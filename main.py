import time
import os

try:
    import cv2
    from hand_tracking import HandDetector
except:
    print("please pip install cv2")

capture = cv2.VideoCapture(0)
frameH = capture.set(3, 640)
frameW = capture.set(4, 480)
detector = HandDetector(maxHands=1)

imglist = []

folder = "assets"
lsd = os.listdir(folder)
print(lsd)
for img in lsd:
    image = cv2.imread(f'{folder}/{img}')
    imglist.append(image)

while True:
    _, frame = capture.read()
    hand_positions = detector.findHands(frame)
    lmlist = detector.findPosition(hand_positions)


    fingers = detector.fingersUp()
    print(fingers)
    if len(fingers) > 0:

        if fingers[0] == 0 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
            frame[0:200, 0:200] = imglist[0]
            print("all finger down")
        if fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
            frame[0:200, 0:200] = imglist[1]

        if fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0 and fingers[4] == 0:
            frame[0:200, 0:200] = imglist[2]

        if fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 0:
            frame[0:200, 0:200] = imglist[3]

        if fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:
            frame[0:200, 0:200] = imglist[4]

        if fingers[0] == 1 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:
            frame[0:200, 0:200] = imglist[5]







    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()