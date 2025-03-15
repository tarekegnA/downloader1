# API Documentation

## `Aria2Downloader`
### `add_download(url, options=None)`
- Adds a new download to **aria2**.
- **Parameters:**  
  - `url` (str) – File URL  
  - `options` (dict) – Download options (e.g., directory)  
- **Returns:** JSON response  

### `pause_download(gid)`
- Pauses a download.  
- **Parameters:**  
  - `gid` (str) – Download ID  
- **Returns:** JSON response  

### `resume_download(gid)`
- Resumes a paused download.  
- **Parameters:**  
  - `gid` (str) – Download ID  
- **Returns:** JSON response  

### `remove_download(gid)`
- Removes a download.  
- **Parameters:**  
  - `gid` (str) – Download ID  
- **Returns:** JSON response  
