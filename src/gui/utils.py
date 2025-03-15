import os
import subprocess

def open_file(file_path):
    """Open the file with the default application."""
    try:
        if os.name == "nt":  # Windows
            os.startfile(file_path)
        elif os.name == "posix":  # macOS or Linux
            subprocess.run(["open", file_path])  # macOS
            # subprocess.run(["xdg-open", file_path])  # Linux
    except Exception as e:
        print(f"Failed to open file: {e}")

def get_file_type(file_name):
    """Get the file type based on the file extension."""
    file_extension = file_name.split(".")[-1].lower()
    if file_extension in ["pdf"]:
        return "PDF"
    elif file_extension in ["mp4", "mkv", "avi"]:
        return "MP4"
    elif file_extension in ["zip", "rar", "tar", "gz"]:
        return "ZIP"
    else:
        return "Other"