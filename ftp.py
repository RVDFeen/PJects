from ftplib import FTP
from collect_and_return import *

def connect_ftp(usrname, password, ip):
    ftp = FTP(ip, usrname, password, None, 1)
    ftp.connect()
    ftp.login(usrname, password)

def upload_files(local_root_dir):
    files = collect_files(local_root_dir)
    print(files)