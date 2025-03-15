import json
import requests
import os

ARIA2_RPC_URL = "http://localhost:6800/jsonrpc"

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

def add_download(url, download_folder):
    """Add a download using aria2 JSON-RPC and categorize files by type."""
    file_name = os.path.basename(url).split("?")[0]
    file_type = get_file_type(file_name)
    save_folder = os.path.join(download_folder, file_type)

    # Create the subfolder if it doesn't exist
    os.makedirs(save_folder, exist_ok=True)

    # Add the download with the specified save folder
    payload = {
        "jsonrpc": "2.0",
        "id": "qwer",
        "method": "aria2.addUri",
        "params": [[url], {"dir": save_folder, "out": file_name}],  # Save to the categorized folder
    }
    response = requests.post(ARIA2_RPC_URL, json=payload)
    return response.json()