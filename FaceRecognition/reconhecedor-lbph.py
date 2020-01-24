import cv2
detectorFace = cv2.CascadeClassifier("haarcascade-frontalface-default.xml")

reconhecedor = cv2.face.LBPHFaceRecognizer_create()
reconhecedor.read("classificadorLBPH.yml")
largura,altura = 220,220
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
cam = cv2.VideoCapture('C:Users\ROBERTO\Pictures\Pic')

while 1:
    conectado,imagem = cam.read()
    imagemCinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
    facesDetectadas = detectorFace.detectMultiScale(imagemCinza,scaleFactor=1.5, minSize=(30,30))

    for (x,y,l,a) in facesDetectadas:
        imagemFace = cv2.resize(imagemCinza[y:y+a, x:x+l],(largura,altura))
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
        id,confianca = reconhecedor.predict(imagemFace)
        nome=''
        if id == 1 :
            nome = 'Gabriel'
        elif id == 2:
            nome = 'Camilla'
        elif id == 3:
            nome = 'Joana'
        cv2.putText(imagem,nome,(x,y+(a+30)),font,2,(0,0,255))
        conf = str(confianca)
        cv2.putText(imagem,conf[:5],(x,y + (a+50)),font,1,(0,255,220))
    cv2.imshow("face" , imagem)
    cv2.waitKey(15)

cam.release()
cv2.destroyAllWindows()