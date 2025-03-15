import json
import os

CONFIG_FILE = "config/default.json"

default_settings = {
    "download_path": "downloads",
    "max_parallel_downloads": 3
}

def load_settings():
    """ Loads settings from a JSON file. """
    if not os.path.exists(CONFIG_FILE):
        save_settings(default_settings)
    with open(CONFIG_FILE, "r") as file:
        return json.load(file)

def save_settings(settings):
    """ Saves settings to a JSON file. """
    os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
    with open(CONFIG_FILE, "w") as file:
        json.dump(settings, file, indent=4)

settings = load_settings()
