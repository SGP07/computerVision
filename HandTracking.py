import cv2, mediapipe as mp, time



class handDetector:
    def __init__(self, mode = False, maxHands = 2, modelComplexity=1, detectConf = 0.5, trackConf = 0.5) :
        
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplexity = modelComplexity
        self.detectConf = detectConf
        self.trackConf = trackConf

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplexity, self.detectConf, self.trackConf)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw: self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

        return img

    def findPosition(self, img, handNum=0, draw=True):

        self.lmList = []

        if self.results.multi_hand_landmarks:
            hand1 = self.results.multi_hand_landmarks[handNum]
            for id, lm in enumerate(hand1.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        
            return self.lmList

    def fingersUp(self):
        #check if thumb is up, if point 4 is on the side (comparing X axis of 4 with 3)
        fingers, tipIds = [], [8, 12, 16, 20]
        if self.lmList[4][1] > self.lmList[3][1]:
            fingers.append(1)
        else :
            fingers.append(0)

        for id in tipIds:
            if self.lmList[id][2] < self.lmList[id-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers

# cap = cv2.VideoCapture(0)
# pTime, cTime = 0, 0
# detector = handDetector()

# while True:
#     success, img = cap.read()
#     img = detector.findHands(img) 
#     lmList = detector.findPosition(img, 0, False)
    
#     if lmList != None:
#         fingers = detector.fingersUp()
#         print(fingers)
    
#     cTime = time.time()
#     fps = 1/(cTime-pTime)
#     pTime = cTime

#     cv2.putText(img, f"{int(fps)} fps", (10, 70), 1, cv2.FONT_HERSHEY_COMPLEX, (255, 0, 0), 3)
    
#     cv2.imshow("Image", img)
#     cv2.waitKey(1)
