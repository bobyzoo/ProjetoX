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

    def main(self):
        
        sample = 0

        classifier = cv2.CascadeClassifier("FaceRecognition/haarcascade-frontalface-default.xml")
        classifierEye = cv2.CascadeClassifier("haarcascade-eye.xml")
        recognation = cv2.face.EigenFaceRecognizer_create()
        width, height = 220, 220
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        cam = cv2.VideoCapture(0)

        while True:
            conn, image = cam.read()
            imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            facesDetectadas = classifier.detectMultiScale(imageGray, scaleFactor=1.5, minSize=(30, 30))

            for (x, y, l, a) in facesDetectadas:
                # cv2.circle(image,(x,y),5,(255,255,0),2)
                # cv2.circle(image,(x+l,y+a),5,(255,255,0),2)
                cv2.rectangle(image, (x, y), (x + l, y + a), (0, 0, 255), 2)
                region = image[y:y + a, x:x + l]
                eyeRegion = cv2.cvtColor(region, cv2.COLOR_BGR2GRAY)
                eyesDetected = classifierEye.detectMultiScale(eyeRegion)
                for (ox, oy, ol, oa) in eyesDetected:
                    cv2.rectangle(region, (ox, oy), (ox + ol, oy + oa), (0, 255, 0), 2)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        imageFace = cv2.resize(imageGray[y:y + a, x:x + l], (width, height))
                        cv2.imshow("face2", imageFace)
                        cv2.imwrite("img/person." + str(id) + '.' + str(sample) + '.jpg', imageFace)
                        print("img/person." + str(id) + '.' + str(sample) + '.jpg')
                        sample += 1
            cv2.imshow("Face", image)
            cv2.waitKey(1)
            phrase = MicrophoneMonitor.monitor_microphone(self.name)
            self.executa_comandos(phrase)
