import unittest
from SerialCommunication.SerialCom import *


class TestSerialCom(unittest.TestCase):

    def test_con(self):
        serial = SerialCom()
        self.assertTrue(serial.get_com().is_open)
        serial.close()

    def test_write(self):
        serial = SerialCom()
        self.assertEqual(serial.write('teste'),5)
        serial.close()

if __name__ == '__main__':
    unittest.main()
