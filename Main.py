from AssistantAI import *
from FaceRecognition.FaceRecognition import *
import threading

Assist = AssistantAI('rose')

cam = FaceRecognition

face = threading.Thread(target=cam.main)

face.start()
while True:
    pass
