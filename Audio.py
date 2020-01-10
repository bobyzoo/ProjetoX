import pyttsx3

class Audio():
    def __init__(self) -> None:
        self.speak = pyttsx3.init()
        super().__init__()

    def cria_audio(self, mensagem):
        self.speak.setProperty('rate', 150)
        self.speak.say(mensagem)
        self.speak.runAndWait()

