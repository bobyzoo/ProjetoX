import cv2
sample = 0

classifier = cv2.CascadeClassifier("haarcascade-frontalface-default.xml")
classifierEye = cv2.CascadeClassifier("haarcascade-eye.xml")
recognation = cv2.face.EigenFaceRecognizer_create()
width,height = 220,220
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
cam = cv2.VideoCapture(0)

id = input('Enter person id: ')
while True:
    conn, image = cam.read()
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    facesDetectadas = classifier.detectMultiScale(imageGray, scaleFactor=1.5, minSize=(150, 150))

    for (x, y ,l,a) in facesDetectadas:
        cv2.rectangle(image, (x,y) , (x+l, y+a) , (0,0,255) , 2)
        region = image[y:y + a, x:x +l]
        eyeRegion = cv2.cvtColor(region,cv2.COLOR_BGR2GRAY)
        eyesDetected = classifierEye.detectMultiScale(eyeRegion)
        for(ox,oy,ol,oa) in eyesDetected:
            cv2.rectangle(region, (ox,oy) ,(ox+ol,oy+oa), (0,255,0) ,2)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                imageFace = cv2.resize(imageGray[y:y +a , x:x +l], (width,height))
                cv2.imshow("face2",imageFace)
                cv2.imwrite("img/person." + str(id) + '.' + str(sample) + '.jpg',imageFace)
                print("img/person." + str(id) + '.' + str(sample) + '.jpg')
                sample+=1
    cv2.imshow("Face", image)
    cv2.waitKey(1)
cam.realese()
cv2.destroyAllWindows()
