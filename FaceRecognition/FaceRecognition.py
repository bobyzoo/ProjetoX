import cv2


class FaceRecognition():
    

    def cam(self):
        conectado,imagem = self.cam.read()
        imagemCinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
        facesDetectadas = self.detectorFace.detectMultiScale(imagemCinza,scaleFactor=1.5, minSize=(30,30))
        for (x,y,l,a) in facesDetectadas:
            imagemFace = cv2.resize(imagemCinza[y:y+a, x:x+l],(self.largura,self.altura))
            cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
            id,confianca = self.reconhecedor.predict(imagemFace)
            nome=''
            if id == 1 :
                nome = 'Gabriel'
            elif id == 2:
                nome = 'Camilla'
            elif id==3:
                nome = 'Joana'
            cv2.putText(imagem,nome,(x,y+(a+30)),self.font,2,(0,0,255))
            cv2.putText(imagem,str(confianca),(x,y + (a+50)),self.font,2,(0,255,220))
        cv2.imshow("face" , imagem)
        cv2.waitKey(15)

    def closeCam(self):
        self.cam.release()
        cv2.destroyAllWindows()
Face = FaceRecognition()
Face.cam()
Face.closeCam()