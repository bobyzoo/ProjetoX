from importacoes import *
import cv2

class AssistantAI:

    def __init__(self, name='rose'):

        super().__init__()
        self.name = name
        self.Assist = classBot('Assistente.db',mode_train=False)

    # executa commandos diversos
    def executa_comandos(self, trigger):
        if 'notícias' in trigger:
            return (Notices.lastNotices())
        elif ('tempo' in trigger or 'temperatura' in trigger) and 'agora' in trigger:
            return (Weather.currentTemperature())
        elif ('tempo' in trigger or 'temperatura' in trigger) and 'hoje' in trigger:
            return (Weather.weatherForecast())
        elif 'toca' in trigger and 'playlist' in trigger:
            return self.playlist('mundanos')
        elif 'dia' in trigger and 'hoje' in trigger:
            return self.data(dia=True)

        elif 'horas' in trigger:
            return self.data(horas=True)
        elif 'led' in trigger and ' liga' in trigger:
            return self.led(1)
        elif 'led' in trigger and ' desliga' in trigger:
            return self.led(0)
        elif 'musica' in trigger and ' toca' in trigger:
            return self.led(0)
        elif 'repita' in trigger or 'diga' in trigger:
            return self.repete(trigger)
        else:
            procura = self.Assist.procuraResposta(trigger)
            print(procura)
            if procura != 0:
                return procura
            else:
                menssagem = trigger.strip(self.Assist)
                return (menssagem)

    #####FUNÇÕES COMANDOS####

    def playlist(self, album):
        if album == 'mundanos':
            browser.open('https://open.spotify.com/playlist/1q54dfQ6DcEARFZm6aarQb')
        else:
            menssagem = 'O album ' + album + ' não foi encontrado'
            return (menssagem)
            print(menssagem)

    def data(self, horas=False, dia=False):
        now = datetime.now()
        if (horas == True):
            menssagem = f'Agora são {now.hour} horas e {now.minute} minutos.'
            return (menssagem)
            print(menssagem)
        elif (dia == True):
            menssagem = f'Hoje é dia {now.day} do {now.month} de {now.year}'
            print('retornou')
            return (menssagem)
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
        return ('musica Star Wars')
        # conexao.write(b'1')

    def repete(self, frase):
        fraseArrumada = frase.replace('rose repita ', ' ')
        print(frase)
        return (fraseArrumada)


