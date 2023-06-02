import os
import glob
from time import sleep
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
device_file1 = '/sys/bus/w1/devices/28-03079794305e/w1_slave'
device_file2 = '/sys/bus/w1/devices/28-030a979448f3/w1_slave'

def read_temp_raw1():
    f = open(device_file1, 'r')
    lines1 = f.readlines()
    f.close()
    return lines1
def read_temp_raw2():
    f = open(device_file2, 'r')
    lines2 = f.readlines()
    f.close()
    return lines2
def read_temp1():
    lines1 = read_temp_raw1()
    while lines1[0].strip()[-3:] != 'YES':
        sleep(0.2)
        lines1 = read_temp_raw1()
    equals_pos = lines1[1].find('t=')
    if equals_pos != -1:
        temp_string1 = lines1[1][equals_pos + 2:]
        temp_c1 = float(temp_string1) / 1000.0
        return temp_c1
    
def read_temp2():
    lines2 = read_temp_raw2()
    while lines2[0].strip()[-3:] != 'YES':
        sleep(0.2)
        lines2 = read_temp_raw2()
    equals_pos = lines2[1].find('t=')
    if equals_pos != -1:
        temp_string2 = lines2[1][equals_pos + 2:]
        temp_c2 = float(temp_string2) / 1000.0
        return temp_c2
try:
    while True:
        print("t1=" + str(read_temp1()))
        print("t2=" + str(read_temp2()))
        sleep(3)
except KeyboardInterrupt:
    pass