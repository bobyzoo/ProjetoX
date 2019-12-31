from gtts import gTTS
from playsound import playsound
import os
class Audio():
    def __init__(self) -> None:
        self.c = 0
        super().__init__()

    def cria_audio(self,mensagem):
        self.c+=1
        tts = gTTS(mensagem, lang='pt-br')
        caminho = 'audio/mensagem' + str(self.c) + '.mp3'
        tts.save(caminho)
        print(mensagem)
        playsound(caminho)
        os.remove(caminho)

