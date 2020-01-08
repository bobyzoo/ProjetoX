import cv2

import numpy
amostra = 0



classificador = cv2.CascadeClassifier("ReconhecimentoFacial/haarcascade-frontalface-default.xml")
classificadorOlho = cv2.CascadeClassifier("ReconhecimentoFacial/haarcascade-eye.xml")
classificadorSorriso = cv2.CascadeClassifier("ReconhecimentoFacial/haarcascade_smile.xml")
reconhecedor = cv2.face.EigenFaceRecognizer_create()
# reconhecedor.read("classificadorEigen.yml")
largura,altura = 220,220
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
cam = cv2.VideoCapture('C:Users\ROBERTO\Pictures\Pic')

id = 1
while True:
    conectado, imagem = cam.read()
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(30, 30))

    for (x, y ,l,a) in facesDetectadas:
        print(x,y)
        print(l,a)
        cv2.circle(imagem,(x,y),5,(255,255,0),2)
        cv2.circle(imagem,(x+l,y+a),5,(255,255,0),2)
        # cv2.rectangle(imagem, (x,y) , (x+l, y+a) , (0,0,255) , 2)
        regiao = imagem[y:y + a, x:x +l]
        regiaoCinzaOlho = cv2.cvtColor(regiao,cv2.COLOR_BGR2GRAY)
        olhosDetectados = classificadorOlho.detectMultiScale(regiaoCinzaOlho)
        # sorriso = classificadorSorriso.detectMultiScale(regiaoCinzaOlho)

        for(ox,oy,ol,oa) in olhosDetectados:
            # cv2.rectangle(regiao, (ox,oy) ,(ox+ol,oy+oa), (0,255,0) ,2)
            if cv2.waitKey(15):
                # print(amostra)
                imagemFace = cv2.resize(imagemCinza[y:y +a , x:x +l], (largura,altura))
                cv2.imwrite("ReconhecimentoFacial/img/pessoa." + str(id) + '.' + str(amostra) + '.jpg',imagemFace)
                amostra+=1
        # for (sx, sy, sl, sa) in sorriso:
        #     cv2.rectangle(regiao, (sx, sy), (sx + sl, sy + sa), (0, 255, 0), 2)
        #     if cv2.waitKey(15):
        #         if numpy.average(imagemCinza) > 110:
        #             imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
        #             print('sorrindo')
        #             # cv2.imwrite("img/pessoa." + str(id) + '.' + str(amostra) + '.jpg',imagemFace)
        #             amostra += 1
        #         else:
        #             print('triste')
    cv2.imshow("Face", imagem)
    # cv2.waitKey(15)
    # if amostra>= numeroAmostra + 1 :
    #     break
print('faces capturadas!')
cam.realese()
cv2.destroyAllWindows()
