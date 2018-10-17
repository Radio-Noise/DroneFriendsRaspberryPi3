import serial
from time import sleep
ser = serial.Serial('/dev/ttyUSB0', 115200)
print(ser)

while 1:
    print('ready')
    ser.write(b'hello\r\n')
    print('      submit')
    sleep(5)
ser.close()
