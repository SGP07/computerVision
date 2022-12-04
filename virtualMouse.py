import cv2, time
import HandTracking as ht
import numpy as np
import math
from subprocess import call

#set up
wCam, hCam = 640, 480

wScreen, hScreen = 1920, 1080

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0 #previous time
detector = ht.handDetector(detectConf=0.65, trackConf=0.65)


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img) 
    lmList = detector.findPosition(img, 0, False)

    if lmList != None:        
        index = lmList[8][1:]
        thumb = lmList[4][1:]
        pinky = lmList[20][1:]
    
        cv2.circle(img, index, 10, (255, 0, 255), cv2.FILLED)

        fingers = detector.fingersUp()
        length = math.hypot(thumb[0]-pinky[0], thumb[1]-pinky[1])

        cursor = np.interp(index[0], (0, wCam), (0, wScreen)), np.interp(index[1], (0, wCam), (0, wScreen))    
    
        if fingers[1] == 1:
            print('Aiming', cursor)
        
        if length < 40:
            print('SHOOT pew pew')
       
    

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f"{int(fps)} fps", (10, 70), 1, cv2.FONT_HERSHEY_COMPLEX, (255, 0, 0), 3)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)