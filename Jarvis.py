from BrainIA import *
import datetime
from Audio import *
from Notices import *
from SpotifyAPI.main import *


class Jarvis(MainBrain, Audio):
    def __init__(self, train_mode=False) -> None:
        super().__init__()
        self.train_mode = train_mode
        self.spotify = Spotify()

    def listener(self, command):

        context = self.brain(command)
        response, id_action, index = self.search_response(context, self.format_command(command))

        if index > 1:
            print(index)
            if self.train_mode and index != 3:
                self.learn_new_call_command(command, id_action)
            self.execute_command(command, id_action)
        else:
            print(index)
            self.speaker('Não entendi')

    def speaker(self, message):
        self.cria_audio(message)

    def execute_command(self, command, id_action):
        if id_action == 1:
            # Verificar hora atual
            now = datetime.datetime.now()
            print(f'Agora são {now.hour} horas e {now.minute} minutos.')
            self.speaker(f'Agora são {now.hour} horas e {now.minute} minutos.')
        elif id_action == 2:
            # Verifica as ultimas noticias
            self.speaker(Notices.lastNotices())
        elif id_action == 5:
            # Inicializa spotify
            self.speaker(self.spotify.player())



jarvis = Jarvis(train_mode=True)

jarvis.listener('Toca Spotify')

import time

time.sleep(5)
jarvis.listener('Para a música no Spotify')
jarvis.spotify.pause()
time.sleep(5)
jarvis.spotify.resume()