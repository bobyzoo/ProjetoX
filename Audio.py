import pyttsx3


class Audio(object):
    def __init__(self):
        self.speak = pyttsx3.init()

    def cria_audio(self, mensagem):
        self.speak.setProperty('rate', 150)
        self.speak.say(mensagem)
        self.speak.runAndWait()
