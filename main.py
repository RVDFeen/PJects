from Filehandler import *
from ftp import *
from Network_Handler import *

user = "httpadmin"
password = "fhttpadmin"
ip = "172.16.0.1"
subnet = "255.255.0.0"

def simple_upload():
    ftp = FTP(ip, user, password, None, 1)
    extract_zip()
    local_dir = get_local_dir()
    connect_ftp(ftp, user, password)
    upload_files(local_dir, ftp)
    disconnect(ftp)
    del_cache()

def create_connection():
    pass

simple_upload()