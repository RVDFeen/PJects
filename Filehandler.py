from zipfile import ZipFile
from shutil import rmtree
import os

zip_file = "zip_test.zip"
cache = "./Cache"
check_file = "index.html"

def extract_zip():
    ZipFile(zip_file).extractall(cache)

def del_cache():
    rmtree(cache)

def get_local_dir():
    location = None

    for root, dirs, files in os.walk(cache):
        for file in files:
            if file == check_file:
                if location == None:
                    location = root
                else:
                    del_cache()
                    exit("Error loading files, try again")
    if location == None:
        exit("Error, No files found")
    return location