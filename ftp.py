from ftplib import FTP
from enum import Enum, auto
from dataclasses import dataclass
import os

SKIP_EXT = {".tmp", ".bak", ".old"}
FLASH_ROOT = "/usr/local/www/flash"
file_data_list = []

def compute_remote_path(file, dir):
    if file.lower().endswith(".cgi"):
        print("found .cgi")
        return (f"{FLASH_ROOT}/usr-cgi")
    if any(file.lower().endswith(ext) for ext in (".dat", ".conf")):
        print(f"found {file}")
        return (f"{FLASH_ROOT}/etc/sysconfig")
    return (f"{FLASH_ROOT}/http/{dir.replace(os.sep, '/')}")

def collect_file_data(root):
    for dirpath, dirnames, files in os.walk(root):
        for file in files:
            local_p = os.path.join(dirpath, file)
            lower_name = file.lower()
            path = os.path.relpath(dirpath, root)
            L_path = os.path.join(dirpath, file)
            R_path = compute_remote_path(file, path)
            file_data_list.append({"File": file, "local_path": L_path, "remote_path": R_path})
    return file_data_list

def connect_ftp(ftp, username, password):
    ftp.connect()
    ftp.login(username, password)

def upload_files(local_root_dir, ftp):
    files = collect_file_data(local_root_dir)
    last_dir = None
    dir_list = []
    for file in files:
        if last_dir != file["remote_path"]:
            ftp.cwd("/")
            if not file["remote_path"] in dir_list:
                print(file["remote_path"])
                try:
                    ftp.mkd(file["remote_path"])
                except Exception as e:
                    print(e)
                dir_list.append(file["remote_path"])
            ftp.cwd(file["remote_path"])
        with open(file["local_path"], "rb") as current_file:
            ftp.storbinary(f"STOR {file["File"]}", current_file)

def disconnect():
    try:
        ftp.quit()
    except Exception as e:
        print(e)
        pass