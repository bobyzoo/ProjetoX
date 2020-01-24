import cv2
import os
import numpy as np

eigenface = cv2.face.EigenFaceRecognizer_create(num_components=50,threshold=0)
fisherface = cv2.face.FisherFaceRecognizer_create()
lbph = cv2.face.LBPHFaceRecognizer_create()


def getImagemComId():
    caminhos = [os.path.join('img', f) for f in os.listdir('img')]

    faces = []
    ids = []
    for caminhoImagem in caminhos:
        imagemFace = cv2.cvtColor(cv2.imread(caminhoImagem),cv2.COLOR_BGR2GRAY)
        id = int(os.path.split(caminhoImagem)[-1].split('.')[1])
        print(id)
        cv2.imshow("Face",imagemFace)
        cv2.waitKey(15)
        faces.append(imagemFace)
        ids.append(id)
    return np.array(ids), faces

ids,faces = getImagemComId()

print('Treinando.... ')
eigenface.train(faces,ids)
eigenface.write('classificadorEigen.yml')



print('pronto')