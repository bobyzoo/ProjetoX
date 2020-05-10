import serial
import time


class SerialCom:
    def __init__(self, port='COM3', speed=9600) -> None:
        self.__com = serial.Serial(port, speed)
        super().__init__()

    def getCom(self):
        return self.__com

    def setCom(self, port, speed):
        self.__com = serial.Serial(port, speed)

    def write(self, message):
        time.sleep(0.002)
        self.getCom().write(str.encode(message))

    def close(self):
        return self.__com.close()
