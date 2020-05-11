import serial
import time


class SerialCom:
    def __init__(self, port='COM3', speed=9600) -> None:
        self.__com = serial.Serial(port, speed)
        super().__init__()

    def get_com(self):
        return self.__com

    def set_com(self, port, speed):
        self.__com = serial.Serial(port, speed)
        return self.__com

    def write(self, message):
        time.sleep(0.002)
        return self.get_com().write(str.encode(message))

    def close(self):
        return self.__com.close()

