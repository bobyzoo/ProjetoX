from Jarvis import *
from microphoneMonitor import *

jarvis = Jarvis(train_mode=True)
heard = MicrophoneMonitor()

while 1:
    command = heard.monitor_microphone(jarvis.name)
    jarvis.listener(command)
