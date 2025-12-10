from Filehandler import *
from ftp import *

user = "httpadmin"
password = "fhttpadmin"
ip = "172.16.0.1"
subnet = "255.255.0.0"

def main():
    extract_zip()
    local_dir = get_local_dir()
    connect_ftp(user, password, ip)
    upload_files(local_dir)
    del_cache()
main()