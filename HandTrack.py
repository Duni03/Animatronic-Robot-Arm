import cv2
import cvzone.SerialModule
from cvzone.HandTrackingModule import HandDetector
import serial

#fi = open('record.txt', 'x')

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

detect = HandDetector(detectionCon=0.8,maxHands=1)
ms=cvzone.SerialModule.SerialObject("COM3",9600,1)

while True:
    stat,img = cap.read()
    img = cv2.flip(img, 1)
    hand,img = detect.findHands(img,flipType=False)
    if hand:
        h=hand[0]
        f = detect.fingersUp(h)
        if f[0]==1:
            f[0]=0
        else:
            f[0]=1
        ans=""
        for i in f:
            ans+=str(i)
        print(ans)
        #fi.write(ans+"\n")
        ms.sendData(ans)
    cv2.imshow("image",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#fi.close()