from ftplib import FTP
from enum import Enum, auto
from dataclasses import dataclass
import os
from time import sleep
import sys

def status_update(file, total, status):
        sys.stdout.write('\r')
        # the exact output you're looking for:
        sys.stdout.write(f"{file} out of {total} uploaded | Status: {status}")
    #if file >= total:
        #sys.stdout.flush()

SKIP_EXT = {".tmp", ".bak", ".old"}
FLASH_ROOT = "/usr/local/www/flash"
file_data_list = []

def compute_remote_path(file, dir):
    if file.lower().endswith(".cgi"):
        return (f"{FLASH_ROOT}/usr-cgi")
    if any(file.lower().endswith(ext) for ext in (".dat", ".conf")):
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
        status_update(files.index(file)+1, len(files), file["File"])
        if last_dir != file["remote_path"]:
            ftp.cwd("/")
            if not file["remote_path"] in dir_list:
                try:
                    ftp.mkd(file["remote_path"])
                    status_update(files.index(file)+1, len(files), f"Created path: {file["remote_path"]}")
                except Exception as e:
                    status_update(files.index(file)+1, len(files), e)
                dir_list.append(file["remote_path"])
            ftp.cwd(file["remote_path"])
        with open(file["local_path"], "rb") as current_file:
            ftp.storbinary(f"STOR {file["File"]}", current_file)

def disconnect(ftp):
    try:
        ftp.quit()
        #print("\n\n")
    except Exception as e:
        ## PLACEHOLDER FOR LOG
        pass