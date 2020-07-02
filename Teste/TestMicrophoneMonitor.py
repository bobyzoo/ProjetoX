from Jarvis import *
import unittest

class TestStringMethods(unittest.TestCase):

    def test_microphone(self):
        print('tente falar "Rose o rato roeu a roupa do rei de roma"')
        test = MicrophoneMonitor.monitor_microphone('rose')
        self.assertEqual(test,'rose o rato roeu a roupa do rei de roma')

if __name__ == '__main__':
    unittest.main()