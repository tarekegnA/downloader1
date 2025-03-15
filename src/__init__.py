"""
Downloader Software Package
---------------------------
This package contains modules for managing downloads using Aria2 and Kivy UI.

Modules:
- `main.py`: Entry point for the application.
- `gui.py`: Handles the user interface.
- `downloader.py`: Core logic for downloading files via Aria2.
- `manager.py`: Manages download processes (pause, resume, cancel).
- `utils.py`: Utility functions for file handling and logging.
- `settings.py`: Configuration management.

Author: Your Name
"""

# Import key components for easier access
from .downloader import Aria2Downloader
from .manager import DownloadManager
from .utils import setup_logging



# Initialize logging when the package is imported
setup_logging()
