import cv2
import mediapipe as mp
import time


cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(False,4,1,0.5,0.5)
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0




while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)
    # print(result.multi_hand_landmarks)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id,lm)
                h,w,c = img.shape
                cx,cy = int(lm.x*w) , int(lm.y*h)
                print(id,cx,cy)
                if id == 8:
                    cv2.circle(img, (cx,cy), 15 ,(0,0,255), cv2.FILLED)


            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)


    #for fps calculation and display
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)) , (5,40) , cv2.FONT_HERSHEY_SIMPLEX , 1 , (255,0,255) , 2)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    # stop when Q is pressed
    if key == 81 or key == 113:
        break
print("code completed")
