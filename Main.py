from AssistantAI import *
from Audio import *
import queue

from FaceRecognition.FaceRecognition import *
from microphoneMonitor import *
import threading

queues = queue.Queue()


def cria_assist(comando):
    Assist = AssistantAI('rose')
    comando = comando.replace('Comando: ', '')
    return Assist.executa_comandos(comando)


cam = FaceRecognition()
face = threading.Thread(target=cam.main, )

mic = MicrophoneMonitor()
audio_capture = threading.Thread(target=lambda q, arg1: q.put(mic.monitor_microphone(arg1)), args=(queues, 'rose'))

audio = Audio()

face.start()
audio_capture.start()

while 1:
    result = queues.get()
    try:
        if not 'Comando:' in result:
            print(result)
            audio.cria_audio(result)
    except:
        print('erro')

    if not audio_capture.is_alive():
        arquivo = open('arq01.txt', 'r')
        nome = arquivo.read()
        print(nome)
        if(nome == "Nao indentificado\n"):
            audio.cria_audio('Não posso te responder se eu não te ver!')
            assistent = threading.Thread(target=lambda q, arg1: q.put(cria_assist(arg1)),
                                         args=(queues, result))
            assistent.start()

            audio_capture = threading.Thread(target=lambda q, arg1: q.put(mic.monitor_microphone(arg1)),
                                             args=(queues, 'rose'))
            audio_capture.start()
        else:
            assistent = threading.Thread(target=lambda q, arg1: q.put(cria_assist(arg1)),
                                     args=(queues, result))
            assistent.start()

            audio_capture = threading.Thread(target=lambda q, arg1: q.put(mic.monitor_microphone(arg1)),
                                         args=(queues, 'rose'))
            audio_capture.start()
