import requests

ARIA2_RPC_URL = "http://localhost:6800/jsonrpc"

def pause_download(gid):
    payload = {"jsonrpc": "2.0", "id": "qwer", "method": "aria2.pause", "params": [gid]}
    return requests.post(ARIA2_RPC_URL, json=payload).json()

def resume_download(gid):
    payload = {"jsonrpc": "2.0", "id": "qwer", "method": "aria2.unpause", "params": [gid]}
    return requests.post(ARIA2_RPC_URL, json=payload).json()

def remove_download(gid):
    payload = {"jsonrpc": "2.0", "id": "qwer", "method": "aria2.remove", "params": [gid]}
    return requests.post(ARIA2_RPC_URL, json=payload).json()
