from zipfile import ZipFile as zip
import os
from ftplib import FTP


path_to_zip_file = "zip_test.zip"
directory_to_extract_to = "./tpm"
FLASH_ROOT = "/usr/local/www/flash"

user = "httpadmin"
password = "fhttpadmin"
ip = "172.16.0.1"
subnet = "255.255.0.0"

dirp = None
filedict = []

normal_task = []
sys_task = []
cgi_task = []



def zip_extract():
    with zip(path_to_zip_file) as cur_zip:
        cur_zip.extractall(directory_to_extract_to)
        
def target():
    fname = os.path.basename(rel_path)

def target(fname):
    if fname.lower().endswith(".cgi"):
        return cgi_task
    if fname.lower().endswith(".dat"):
        return sys_task
    return normal_task

def files():
    for dirpath, _dirnames, flilenames in os.walk(directory_to_extract_to):
        for fname in flilenames:
            lowern = fname.lower()
            path = os.path.join(dirpath, lowern)
            fkind = target(fname)
            fkind.append(path)
            filedict.append({"name": lowern, "local_path": path})
    print(filedict)

def upload_file(targetname):
    print(targetname, len())

def ftp_main():
    print("unpacking zip")
    zip_extract()
    print("collecting files")
    files()
    print("start connection, \nDont disconnet while connection is active")
    ftp = FTP(ip,user,password, None, 1)
    ftp.connect()
    ftp.login(user, password)
    print("connection succesfull")
    print(f"start uploading {len(normal_task + sys_task + cgi_task)} files")
    if normal_task != []:
        dir = f"{FLASH_ROOT}/http/"
        print("normal_task")

        ftp.cwd(dir)
        for i in normal_task:
            upload_file(i)

    if sys_task != []:
        dir = f"{FLASH_ROOT}/etc/sysconfig/"
        print("sys_task")

        ftp.cwd(dir)

    if cgi_task != []:
        dir = f"{FLASH_ROOT}/usr-cgi"
        print("cgi_task")

        ftp.cwd(dir)

ftp_main()
