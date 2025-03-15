from kivy.app import App
from .ui import DownloaderUI

class DownloaderApp(App):
    """Main App Class."""

    def build(self):
        return DownloaderUI()  # Return an instance of the main UI