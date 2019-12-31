from importacoes import *

# Iniciando conexao serial

# conexao = serial.Serial('COM3', 9600)

##### CONFIGURAÇÕES
with open('python-Assist-106bd85a8ad1.json') as credenciais:
    credenciais = credenciais.read()



rose = classBot('Assistente.db')
hotword = 'rose'
c = 0

Audio =  Audio()






#####FUNÇÕES PRINCIPAIS#####
def monitora_microfone():

    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        while True:
            print('Aguardando comando: ')
            audio = microfone.listen(source)
            try:
                trigger = (microfone.recognize_google(audio,language='pt'))
                trigger = trigger.lower()
                print(trigger)
                if hotword in trigger:
                    print('Comando: ', trigger)
                    executa_comandos(trigger)
            except sr.UnknownValueError:
                print("Google Cloud Speech não entendeu o audio")
            except sr.RequestError as e:
                responde(trigger)
                print("Could not request results from Google Cloud Speech service; {0}".format(e))
                responde('naoconecta')


def responde(arquivo):
    playsound('audio/'+arquivo+'.mp3')


#executa comandos diversos
def executa_comandos(trigger):

    if 'notícias' in trigger:
        ultimas_noticias()
    elif 'tempo' in trigger and 'agora' in trigger:
        previsao_tempo(tempo=True)
    elif 'tempo' in trigger and 'hoje' in trigger:
        previsao_tempo(minmax=True)
    elif 'toca' in trigger and 'playlist' in trigger:
        playlist('mundanos')
    elif 'dia' in trigger and 'hoje' in trigger:
        data(dia=True)
    elif 'horas' in trigger:
        data(horas=True)
    elif 'led' in trigger and ' liga' in trigger:
        led(1)
    elif 'led' in trigger and ' desliga' in trigger:
        led(0)
    elif 'musica' in trigger and ' toca' in trigger:
        led(0)
    elif 'repita' in trigger or 'diga' in trigger:
        repete(trigger)
    else:

        if rose.procuraResposta(trigger) != 0:
            Audio.cria_audio(rose.procuraResposta(trigger))
        else:
            menssagem = trigger.strip(hotword)
            Audio.cria_audio(menssagem)


    
#####FUNÇÕES COMANDOS####
def ultimas_noticias():
    site = get('https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419')
    noticias = BeautifulSoup(site.text, 'html.parser')
    for item in noticias.find_all('item')[:3]:
        Audio.cria_audio(item.title.text)
def playlist(album):
    if album == 'mundanos':
        browser.open('https://open.spotify.com/playlist/1q54dfQ6DcEARFZm6aarQb')
    else:
        menssagem = 'O album '+album+' não foi encontrado'
        Audio.cria_audio(menssagem)
        print(menssagem)
def previsao_tempo(tempo = False, minmax = False):
    site = get('http://api.openweathermap.org/data/2.5/weather?id=3463237&appid=037ee4a0587c9e792cfaf33c172010e4&units=metric&lang=pt')
    clima = site.json()
    temperatura = clima['main']['temp']
    minima = clima['main']['temp_min']
    maxima = clima['main']['temp_max']
    descricao = clima['weather'][0]['description']
    print(f'{temperatura} {minima} {maxima} {maxima} {descricao}')
    if tempo:
        mensagem = f'No momento está fazendo {temperatura} graus com {descricao} la fora.'

    if minmax:
        mensagem = f'Minima de {minima} graus e máxima de {maxima} graus.'
    Audio.cria_audio(mensagem)
def data(horas=False, dia = False):
    now = datetime.now()
    if(horas == True):
        menssagem = f'Agora são {now.hour} horas e {now.minute} minutos.'
        Audio.cria_audio(menssagem)
        print(menssagem)
    elif(dia == True):
        menssagem = f'Hoje é dia {now.day} do {now.month} de {now.year}'
        Audio.cria_audio(menssagem)
        print(menssagem)

def led(led):

    print(led)
    if(led == 1):
        # conexao.write(b'1')
        pass
    if(led == 0):
        pass
       # conexao.write(b'0')
    #leitura_serial = str(conexao.readline())
    #leitura_serial = leitura_serial[2:12]

def musicaStarWars():
    Audio.cria_audio('musica Star Wars')
    # conexao.write(b'1')


def repete(frase):
    fraseArrumada = frase.replace('rose repita ',' ')
    print(frase)
    Audio.cria_audio(fraseArrumada)


def main():
    #
    # Audio.cria_audio('iniciando assistente virtual')
    # Audio.cria_audio('Olá, Eu sou a Rose')
    monitora_microfone()


main()
