from speech_recognition import Microphone, Recognizer, UnknownValueError, RequestError


class MicrophoneMonitor(object):

    def __init__(self) -> None:
        self.micro = Recognizer()
        self.micro.energy_threshold = 4000
        self.micro.pause_threshold = 0.5

    def monitor_microphone(self, hotword='jarvis'):
        with Microphone() as source:
            self.micro.adjust_for_ambient_noise(source, duration=0.5)
            while True:
                print('Aguardando comando: ')
                audio = self.micro.listen(source)
                try:
                    trigger = self.micro.recognize_google(audio, language='pt')
                    # with open("microphone-results.wav", "wb") as f:
                    #     f.write(audio.get_wav_data())
                    print(trigger)
                    if hotword.lower() in trigger or hotword.capitalize() in trigger:
                        print('Comando: ', trigger)
                        return trigger
                except UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                except RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))
