import os
import threading
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from ..utils import open_file, get_file_type  # Import get_file_type
import downloader
import requests

class DownloadItem(BoxLayout):
    """Represents a single download entry with progress tracking."""

    def __init__(self, url, color_scheme, download_folder, **kwargs):
        super().__init__(orientation="horizontal", size_hint_y=None, height=40, spacing=10, **kwargs)
        self.url = url
        self.file_name = os.path.basename(url).split("?")[0]
        self.progress = 0
        self.downloaded_size = 0
        self.total_size = 0
        self.color_scheme = color_scheme
        self.download_folder = download_folder  # Folder to save the downloaded file

        # File name label
        self.label = Label(text=self.file_name, size_hint_x=0.3, halign="left", color=self.color_scheme["text"])

        # Progress bar
        self.progress_bar = ProgressBar(max=100, size_hint_x=0.4)
        self.update_progress_bar_color()

        # Progress details (percentage, downloaded size, total size, remaining size)
        self.progress_label = Label(text="0%", size_hint_x=0.1, color=self.color_scheme["text"])
        self.downloaded_label = Label(text="0 MB", size_hint_x=0.1, color=self.color_scheme["text"])
        self.total_label = Label(text="0 MB", size_hint_x=0.1, color=self.color_scheme["text"])
        self.remaining_label = Label(text="0 MB", size_hint_x=0.1, color=self.color_scheme["text"])

        # Add widgets to the layout
        self.add_widget(self.label)
        self.add_widget(self.progress_bar)
        self.add_widget(self.progress_label)
        self.add_widget(self.downloaded_label)
        self.add_widget(self.total_label)
        self.add_widget(self.remaining_label)

        # Start the download in a separate thread
        threading.Thread(target=self.start_download, daemon=True).start()

    def update_progress_bar_color(self):
        """Update the progress bar color based on the current theme."""
        with self.progress_bar.canvas.before:
            Color(*self.color_scheme["progress_bar"])
            self.rect = Rectangle(pos=self.progress_bar.pos, size=self.progress_bar.size)
        self.progress_bar.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, instance, value):
        """Update the progress bar's rectangle position and size."""
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def start_download(self):
        """Start the download using aria2 JSON-RPC."""
        try:
            file_type = get_file_type(self.file_name)  # Get the file type
            save_folder = os.path.join(self.download_folder, file_type)  # Categorized folder
            print(f"Saving file to: {save_folder}")  # Debugging: Print the save folder

            # Call the add_download function from downloader.py
            response = downloader.add_download(self.url, save_folder)
            print("Download started:", response)

            # Get the total file size from the response (if available)
            if "result" in response:
                gid = response["result"]  # Get the download GID
                # Fetch download status to get the total file size
                status_payload = {
                    "jsonrpc": "2.0",
                    "id": "qwer",
                    "method": "aria2.tellStatus",
                    "params": [gid],
                }
                status_response = requests.post(downloader.ARIA2_RPC_URL, json=status_payload).json()
                if "result" in status_response:
                    self.total_size = int(status_response["result"]["totalLength"])  # Actual file size in bytes
                else:
                    self.total_size = 0  # Fallback if size is not available
            else:
                self.total_size = 0  # Fallback if response is invalid

            # Simulate progress updates (replace with actual progress tracking)
            while self.progress < 100:
                # Fetch download status to get the current progress
                status_payload = {
                    "jsonrpc": "2.0",
                    "id": "qwer",
                    "method": "aria2.tellStatus",
                    "params": [gid],
                }
                status_response = requests.post(downloader.ARIA2_RPC_URL, json=status_payload).json()
                if "result" in status_response:
                    self.downloaded_size = int(status_response["result"]["completedLength"])  # Downloaded size in bytes
                    if self.total_size > 0:
                        self.progress = int((self.downloaded_size / self.total_size) * 100)  # Calculate progress percentage
                    else:
                        self.progress = 0  # Fallback if total size is not available
                else:
                    self.progress = 0  # Fallback if status is not available

                # Update UI progress
                Clock.schedule_once(self.update_progress, 0)
                threading.Event().wait(0.5)  # Simulate delay

            # Show download complete popup
            Clock.schedule_once(self.download_complete, 0)
        except Exception as e:
            print("Download failed:", e)

    def update_progress(self, dt):
        """Update UI progress."""
        self.progress_bar.value = self.progress
        self.progress_label.text = f"{self.progress}%"
        self.downloaded_label.text = f"{self.downloaded_size / (1024 * 1024):.2f} MB"  # Convert bytes to MB
        self.total_label.text = f"{self.total_size / (1024 * 1024):.2f} MB"  # Convert bytes to MB
        self.remaining_label.text = f"{(self.total_size - self.downloaded_size) / (1024 * 1024):.2f} MB"  # Convert bytes to MB

    def download_complete(self, dt):
        """Show popup after download is complete."""
        file_type = get_file_type(self.file_name)  # Get the file type
        save_folder = os.path.join(self.download_folder, file_type)  # Categorized folder
        file_path = os.path.join(save_folder, self.file_name)  # Full file path

        print(f"File saved at: {file_path}")  # Debugging: Print the file path

        content = BoxLayout(orientation="vertical", spacing=10)
        content.add_widget(Label(text=f"Download Complete! File saved in: {save_folder}", color=self.color_scheme["text"]))

        # Button to open the Downloads folder
        open_folder_button = Button(text="Open Downloads Folder", size_hint_y=None, height=40, background_color=self.color_scheme["button"])
        open_folder_button.bind(on_press=lambda x: os.startfile(save_folder))

        # Button to open the downloaded file
        open_file_button = Button(text="Open File", size_hint_y=None, height=40, background_color=self.color_scheme["button"])
        open_file_button.bind(on_press=lambda x: open_file(file_path))  # Use the open_file function here

        content.add_widget(open_folder_button)
        content.add_widget(open_file_button)

        popup = Popup(
            title="Download Complete",
            content=content,
            size_hint=(0.5, 0.3),
            background_color=self.color_scheme["background"],
        )
        popup.open()

    def apply_color_scheme(self):
        """Apply the current color scheme to the UI."""
        self.label.color = self.color_scheme["text"]
        self.progress_label.color = self.color_scheme["text"]
        self.downloaded_label.color = self.color_scheme["text"]
        self.total_label.color = self.color_scheme["text"]
        self.remaining_label.color = self.color_scheme["text"]
        self.update_progress_bar_color()