import speech_recognition as sr

class MicrophoneMonitor():

    #leave the microphone level between 50 and 60
    @staticmethod
    def monitor_microphone(hotword='rose'):
        micro = sr.Recognizer()
        with sr.Microphone() as source:
            micro.adjust_for_ambient_noise(source)
            while True:
                print('Aguardando comando: ')
                audio = micro.listen(source)
                try:
                    trigger = (micro.recognize_google(audio, language='pt'))
                    trigger = trigger.lower()
                    if hotword in trigger:
                        print('Comando: ', trigger)
                        trigger = 'Comando: '+ trigger
                        return trigger
                except:
                    return 'Não ouvi nada'