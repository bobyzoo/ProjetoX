from BrainIA import *
import datetime
from APIs.Audio.Audio import *
from APIs.Notices.Notices import *
from APIs.SpotifyAPI.main import *
import random


class Jarvis(MainBrain, Audio):

    def __init__(self, train_mode=False, train_chat_mode=False) -> None:
        super().__init__()
        self.spotify = Spotify()
        self.train_mode = train_mode
        self.train_chat_mode = train_chat_mode
        self.name = 'Jarvis'
        if train_chat_mode:
            self.chat_mode()

    def listener(self, command: str) -> None:
        command = command.replace(self.name.lower(), '').replace(self.name.capitalize(), '').strip()
        context = self.brain(command)
        response, id_action, index = self.search_action(context, self.format_command(command))
        if index > 1:
            print(index)
            if self.train_mode and index != 3:
                self.learn_new_call_command(command, id_action)
            self.execute_command(command, id_action)
        else:
            response, id_con, index = self.search_dialog_context(context, self.format_command(command))
            if index > 1:
                if self.train_mode and index != 3:
                    self.learn_new_dialog(command, id_con)
                    print(response)
                self.speaker(response)
            else:
                print('nao entendi')
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
        elif id_action == 10:
            # Pausa spotify
            self.speaker(self.spotify.pause())

    def chat_mode(self):
        print('comeca')
        while 1:
            list = self.selectTable('phrases')
            num = random.randint(0, len(list) - 1)
            phrase = list[num]
            answer = input(phrase[1])

            if not self.verify_phrase(answer):
                self.insert_new_phrase(answer)
                self.insert_phrase_conn(phrase[0], self.getLastId())
            elif not self.verify_phrase_conn(phrase[0], self.getIDPhrase(answer)):
                self.insert_phrase_conn(phrase[0], self.getIDPhrase(answer))
