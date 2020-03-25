from importacoes import *
import cv2

class AssistantAI:

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self.Assist = classBot('Assistente.db',mode_train=True)
        self.Audio = Audio()

    # executa commandos diversos
    def executa_comandos(self, trigger):
        if 'notícias' in trigger:
            self.Audio.cria_audio(Notices.lastNotices())
        elif ('tempo' in trigger or 'temperatura' in trigger) and 'agora' in trigger:
            self.Audio.cria_audio(Weather.currentTemperature())
        elif ('tempo' in trigger or 'temperatura' in trigger) and 'hoje' in trigger:
            self.Audio.cria_audio(Weather.weatherForecast())
        elif 'toca' in trigger and 'playlist' in trigger:
            self.playlist('mundanos')
        elif 'dia' in trigger and 'hoje' in trigger:
            self.data(dia=True)
        elif 'horas' in trigger:
            self.data(horas=True)
        elif 'led' in trigger and ' liga' in trigger:
            self.led(1)
        elif 'led' in trigger and ' desliga' in trigger:
            self.led(0)
        elif 'musica' in trigger and ' toca' in trigger:
            self.led(0)
        elif 'repita' in trigger or 'diga' in trigger:
            self.repete(trigger)
        else:

            if self.Assist.procuraResposta(trigger) != 0:
                
                self.Audio.cria_audio(self.Assist.procuraResposta(trigger))
            else:
                menssagem = trigger.strip(self.Assist)
                self.Audio.cria_audio(menssagem)

    #####FUNÇÕES COMANDOS####

    def playlist(self, album):
        if album == 'mundanos':
            browser.open('https://open.spotify.com/playlist/1q54dfQ6DcEARFZm6aarQb')
        else:
            menssagem = 'O album ' + album + ' não foi encontrado'
            self.Audio.cria_audio(menssagem)
            print(menssagem)

    def data(self, horas=False, dia=False):
        now = datetime.now()
        if (horas == True):
            menssagem = f'Agora são {now.hour} horas e {now.minute} minutos.'
            self.Audio.cria_audio(menssagem)
            print(menssagem)
        elif (dia == True):
            menssagem = f'Hoje é dia {now.day} do {now.month} de {now.year}'
            self.Audio.cria_audio(menssagem)
            print(menssagem)

    def led(self, led):

        print(led)
        if (led == 1):
            # conexao.write(b'1')
            pass
        if (led == 0):
            pass
        # conexao.write(b'0')
        # leitura_serial = str(conexao.readline())
        # leitura_serial = leitura_serial[2:12]

    def musicaStarWars(self):
        self.Audio.cria_audio('musica Star Wars')
        # conexao.write(b'1')

    def repete(self, frase):
        fraseArrumada = frase.replace('rose repita ', ' ')
        print(frase)
        self.Audio.cria_audio(fraseArrumada)


