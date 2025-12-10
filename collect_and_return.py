import os

SKIP_EXT = {".tmp", ".bak", ".old"}
FLASH_ROOT = "/usr/local/www/flash"
files_dir = []

def compute_remote_path(l_path):
    if l_path.lower().endswith(".cgi"):
        return (f"{FLASH_ROOT}/usr-cgi")
    if any(l_path.lower().endswith(ext) for ext in (".dat", ".conf")):
        return (f"{FLASH_ROOT}/etc/sysconfig")
    return (f"{FLASH_ROOT}/http/{l_path.replace(os.sep, '/')}")



def collect_files(root):
    for dirpath, _dirnames, files in os.walk(root):
        for file in files:
            local_p = os.path.join(dirpath, file)
            lower_name = file.lower()
            path = os.path.relpath(dirpath, root)
            L_path = os.path.join(path, file)
            R_path = os.path.join(compute_remote_path(path), file)
            files_dir.append({"local_P":local_p, "remote_p": R_path})
    return files_dir