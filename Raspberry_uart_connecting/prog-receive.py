#coding:utf-8

import serial

path = 'C:Users\LETech\Documents\Procon\Assets\senserdatas\datas.txt'
path_log = 'C:Users\LETech\Documents\Procon\Assets\senserdatas\log.txt'

ser=serial.Serial('COM7',115200)
print(ser)
while 1:
    count = 1
    
    print('wait receive...')
    c=ser.readline()
    print(c)
    tmp = c.decode()

    string = tmp[14:]

    print(string)
    
    with open(path, mode='w') as f:
        f.write(string)

    with open(path_log, mode='a') as f:
        f.write(string)
    
    count = count + 1
    


