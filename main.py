from Filehandler import *
from ftp import *
from Network_Handler import *
from logging import *

##      Gui     ##

from tkinter import *
from tkinter import filedialog

def gui():
    main_window = Tk()
    main_window.geometry("1200x700")
    main_window.title('Pject pcomanager')

    file_path = StringVar(value="")


    user = "httpadmin"
    password = "fhttpadmin"
    ip = '172.16.0.1'
    subnet = "255.255.0.0"

    def Select_zip_file():

        path = filedialog.askopenfilename(
            title='Select zip file',
            filetypes=[("Zip File", ('*.zip'))]
        )

        file_path.set(str(path))
        print(file_path)

    def get_path():
        return file_path.get()
    
    def Upload_zip_file():
        path = get_path()
        try:
            if path == "":
                raise Exception('No zip file selected')
            ftp = FTP(ip, user, password, None, 1)

            extract_zip(path)

            local_dir = get_local_dir()

            connect_ftp(ftp, user, password)
            upload_files(local_dir, ftp)
            disconnect(ftp)
            del_cache()
        except Exception as e:
            print(e)


    Button(main_window, text='Choose Zip', command=Select_zip_file).grid(column=1, row=2)
    Button(main_window, text='Upload Zip', command=Upload_zip_file).grid(column=2, row=2)

    Label(main_window, textvariable=file_path).grid(column=1, row=3)
    main_window.mainloop()
gui()