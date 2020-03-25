

import threading
import time
from FaceRecognition.FaceRecognition import *
from microphoneMonitor import *




def work():
    while True:
        arquivo = open('../../arq01.txt', 'r')
        return arquivo.read()


def microfone():
    mic = MicrophoneMonitor
    while True:
        q = mic.monitor_microphone('rose')
        res = work()
        if(res == 'Não Indentificado\n'):
            print('nao posso responder sem te ver')
        else:
            print('te vi')


face =FaceRecognition()



t = threading.Thread(target=face.main)
micro = threading.Thread(target=microfone)
t.start()
micro.start()
while t.isAlive() or micro.isAlive():
    print ("Aguardando thread")
    time.sleep(5)

print("Thread morreu")
print("Finalizando programa")