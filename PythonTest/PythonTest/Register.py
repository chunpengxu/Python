import os, sys
import time
import wmi
def get_disk_info():
    tmplist=[]
    c=wmi.WMI()
    for physical_disk in c.Win32_DiskDrive():
        tmplist.append(physical_disk.SerialNumber)
        tmplist.append(physical_disk.Caption)
        tmplist.append(str(int(physical_disk.Size)/1024/1024/1024))
        #print(tmplist)
        disk_str=','.join(tmplist)
    return disk_str

def get_cpu_info():
    tmplist=[]
    c=wmi.WMI()
    for computer_cpu in c.Win32_Processor():
        tmplist.append(computer_cpu.ProcessorId)
        cpu_str=' '.join(tmplist)
    return cpu_str

