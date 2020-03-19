import cv2
import os

def saveFaceFrame(userID):
    if not os.path.exists('dataset'): # dataset varsa devam et yoksa oluştur
        os.mkdir('dataset')
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # set video width
    cam.set(4, 480)  # set video height
    faceDetector = cv2.CascadeClassifier('Cascade/haarcascade_frontalface_default.xml')

    print("\n [INFO] Initializing face capture. Look at the camera and wait ...")

    count = 0 # yüz örnekleri sayısı için sayaç (max örnek : 15)

    while (True):
        ret, img = cam.read() # kameradan oku
        img = cv2.flip(img, 2)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # görüntüyü gri yap
        faces = faceDetector.detectMultiScale(gray, 1.3, 5) #gri frame/küçültme ölçeği/koşuluk sayıları
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            count += 1
            # yüzleri dataset dosyasına kaydet
            cv2.imwrite("dataset/User." + str(userID) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])
            cv2.imshow('image', img)
        k = cv2.waitKey(100) & 0xff  # kaydı durdurmak için 'esc' tuşuna bas
        if k == 27:
            break
        elif count >= 15:  # 15 yüz örneği al ve kayıdı durdur
            break
    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()

#saveFaceFrame(1)