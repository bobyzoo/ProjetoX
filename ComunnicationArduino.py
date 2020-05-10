import serial
arduino = serial.Serial('COM3',9600)

import serial  # necessário para importar a biblioteca pyserial
import time
time.sleep(1)
# escreve a string teste nesta porta
while 1:
    arduino.write(b'1')
    time.sleep(1)
    arduino.write(b'0')
    time.sleep(1) 
    # print(arduino.write(b'1'))