import psutil

disk_list = []

for device in psutil.disk_partitions():
    disk_list.append(device.device)

print(disk_list)