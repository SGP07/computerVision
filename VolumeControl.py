import cv2, time
import HandTracking as ht
import numpy as np
import math

#set up
wCam, hCam = 640, 480


cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0 #previous time
detector = ht.handDetector()


while True:
    success, img = cap.read()
    img = detector.findHands(img) 
    lmList = detector.findPosition(img, 0, False)
    if lmList != None:        
        thumb = (lmList[4][1], lmList[4][2])
        index = (lmList[8][1], lmList[8][2])
        center = ((thumb[0]+index[0])//2, (thumb[1]+index[1])//2) 

        cv2.circle(img, thumb, 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, index, 10, (255, 0, 255), cv2.FILLED)
        cv2.line(img, thumb, index, (255, 0, 355), 3)
        cv2.circle(img, center, 8, (255, 0, 255), cv2.FILLED)

        length = math.hypot(thumb[0]-index[0], thumb[1]-index[1])
        print(length)
        if length < 35: cv2.circle(img, center, 8, (255, 0, 0), cv2.FILLED)
        if length > 250: cv2.circle(img, center, 8, (255, 255, 0), cv2.FILLED)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f"{int(fps)} fps", (10, 70), 1, cv2.FONT_HERSHEY_COMPLEX, (255, 0, 0), 3)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)