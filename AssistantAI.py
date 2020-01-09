from importacoes import *

class AssistantAI:

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self.Assist = classBot('Assistente.db')
        self.Audio = Audio()

    # executa commandos diversos
    def executa_comandos(self, trigger):
        if 'notícias' in trigger:
            self.ultimas_noticias()
        elif 'tempo' in trigger and 'agora' in trigger:
            Audio.cria_audio(Weather.currentTemperature())
        elif 'tempo' in trigger and 'hoje' in trigger:
            Audio.cria_audio(Weather.weatherForecast())
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

            if self.assist.procuraResposta(trigger) != 0:
                Audio.cria_audio(self.assist.procuraResposta(trigger))
            else:
                menssagem = trigger.strip(self.Assist)
                Audio.cria_audio(menssagem)

    #####FUNÇÕES COMANDOS####
    def ultimas_noticias(self):
        site = get('https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419')
        noticias = BeautifulSoup(site.text, 'html.parser')
        for item in noticias.find_all('item')[:3]:
            Audio.cria_audio(item.title.text)

    def playlist(self, album):
        if album == 'mundanos':
            browser.open('https://open.spotify.com/playlist/1q54dfQ6DcEARFZm6aarQb')
        else:
            menssagem = 'O album ' + album + ' não foi encontrado'
            Audio.cria_audio(menssagem)
            print(menssagem)

    def data(self, horas=False, dia=False):
        now = datetime.now()
        if (horas == True):
            menssagem = f'Agora são {now.hour} horas e {now.minute} minutos.'
            Audio.cria_audio(menssagem)
            print(menssagem)
        elif (dia == True):
            menssagem = f'Hoje é dia {now.day} do {now.month} de {now.year}'
            Audio.cria_audio(menssagem)
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
        Audio.cria_audio('musica Star Wars')
        # conexao.write(b'1')

    def repete(self, frase):
        fraseArrumada = frase.replace('rose repita ', ' ')
        print(frase)
        Audio.cria_audio(fraseArrumada)

    def main(self):
        while True:
            phrase = MicrophoneMonitor.monitor_microphone(self.Assist)
            self.executa_comandos(phrase)
