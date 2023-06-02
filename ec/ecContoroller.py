import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
threshold_ec_value = 500

def get_ec_value():
    ser.write(b'r')
    time.sleep(1)
    ec_value = int(ser.readline().decode().strip())
    print("testgetecv")
    return ec_value

def turn_on_led():
    ser.write(b't')

while True:
    print("test")
    ec_value = get_ec_value()
    print("test")
    print(f"EC value: {ec_value}")

    if ec_value <= threshold_ec_value:
        isledvalue = turn_on_led()
        print(f"ledValue: {isledvalue}")
    time.sleep(5)