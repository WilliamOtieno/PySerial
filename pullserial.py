import serial
from saveserial import *

ser = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=1)

while True:
    arduinoData = ser.readline().decode("ascii")
    print(arduinoData)
    saveSerialData(arduinoData)
