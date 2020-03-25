import cv2


class FaceRecognition():
    def __init__(self) -> object:
        self.detectorFace = cv2.CascadeClassifier("haarcascade-frontalface-default.xml")
        self.reconhecedor = cv2.face.EigenFaceRecognizer_create()
        self.reconhecedor.read("classificadorEigen.yml")
        self.largura, self.altura = 220, 220
        self.font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        self.cam = cv2.VideoCapture(0)

    def write_text(self, mensagem):
        arquivo = open('arq01.txt', 'w')
        arquivo.write(f"{mensagem}\n")
        arquivo.close()

    def main(self):
        cont = 0
        while 1:
            conectado, imagem = self.cam.read()
            imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
            facesDetectadas = self.detectorFace.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(30, 30))
            nome = 'Não Indentificado'
            for (x, y, l, a) in facesDetectadas:
                imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (self.largura, self.altura))
                cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
                id, confianca = self.reconhecedor.predict(imagemFace)
                if id == 1:
                    nome = 'Gabriel'
                elif id == 2:
                    nome = 'Camilla'
                elif id == 3:
                    nome = 'Joana'
                cv2.putText(imagem, nome, (x, y + (a + 30)), self.font, 2, (0, 0, 255))
                cv2.putText(imagem, str(confianca), (x, y + (a + 50)), self.font, 2, (0, 255, 220))

            cont += 1
            if cont == 60:
                cont = 0
                self.write_text(nome)
            cv2.imshow("face", imagem)
            cv2.waitKey(15)
        cam.release()
        cv2.destroyAllWindows()
