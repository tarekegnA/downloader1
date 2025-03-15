from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window
from .components.download_item import DownloadItem
from .themes import COLOR_SCHEMES
from .utils import open_file
import os

class DownloaderUI(BoxLayout):
    """Main UI layout with input and download list."""

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=10, spacing=10)
        self.color_scheme = COLOR_SCHEMES["light"]  # Default to light mode
        self.download_folder = os.path.expanduser("~/Downloads")  # Folder to save downloaded files

        # URL Input & Download Button (side by side)
        self.input_layout = BoxLayout(size_hint_y=None, height=40, spacing=10)
        self.url_input = TextInput(hint_text="Enter Download URL", size_hint_x=0.7, multiline=False)
        self.download_button = Button(text="Download", size_hint_x=0.3)

        # Add right-click context menu to the URL input field
        self.url_input.bind(on_touch_down=self.show_context_menu)

        # Dark mode toggle button
        self.dark_mode_button = Button(text="Dark Mode", size_hint_y=None, height=40)
        self.dark_mode_button.bind(on_press=self.toggle_dark_mode)

        self.input_layout.add_widget(self.url_input)
        self.input_layout.add_widget(self.download_button)
        self.add_widget(self.input_layout)
        self.add_widget(self.dark_mode_button)

        # Download List (Container)
        self.download_list = BoxLayout(orientation="vertical", size_hint_y=None, spacing=10)
        self.add_widget(self.download_list)

        # Bind the Download button to start_download method
        self.download_button.bind(on_press=self.start_download)

        # Apply the initial color scheme after all widgets are initialized
        self.apply_color_scheme()

    def start_download(self, instance):
        """Start a new download."""
        url = self.url_input.text.strip()
        if url:
            download_item = DownloadItem(url, self.color_scheme, self.download_folder)
            self.download_list.add_widget(download_item)  # Add to the UI
            self.url_input.text = ""

    def show_context_menu(self, instance, touch):
        """Show right-click context menu for the URL input field."""
        if instance.collide_point(*touch.pos) and touch.button == "right":
            from .components.context_menu import create_context_menu
            create_context_menu(instance, self.color_scheme)

    def toggle_dark_mode(self, instance):
        """Toggle between light and dark mode."""
        if self.color_scheme == COLOR_SCHEMES["light"]:
            self.color_scheme = COLOR_SCHEMES["dark"]
            instance.text = "Light Mode"
        else:
            self.color_scheme = COLOR_SCHEMES["light"]
            instance.text = "Dark Mode"
        self.apply_color_scheme()

    def apply_color_scheme(self):
        """Apply the current color scheme to the UI."""
        Window.clearcolor = self.color_scheme["background"]
        self.url_input.foreground_color = self.color_scheme["text"]
        self.download_button.background_color = self.color_scheme["button"]
        self.dark_mode_button.background_color = (0.5, 0.5, 0.5, 1)  # Neutral color for the toggle button

        # Update existing DownloadItem widgets
        for child in self.download_list.children:
            if isinstance(child, DownloadItem):
                child.color_scheme = self.color_scheme
                child.apply_color_scheme()