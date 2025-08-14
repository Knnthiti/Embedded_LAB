import cv2
import numpy as np

countLeft = 0
countRight = 0
tolerance = 2
iframe = 0
diffLeftList = []
diffRightList = []
Left = False
Right = False
prevLeft = False
prevRight = False
thick = 20

cap = cv2.VideoCapture(0)  # initialize the camera
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # get width of video resolution
sensorLeft = int(width * 20 / 100)
sensorRight = int(width * 75 / 100)

firstLeftFrame = None
firstRightFrame = None

while True:  # loop over the frames of the video
    ret, frame = cap.read()  # reading from webcam
    if not ret:
        print("ไม่สามารถอ่านเฟรมจากกล้องได้")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # gray scale

    leftFrame = gray[:, sensorLeft:sensorLeft + thick]
    rightFrame = gray[:, sensorRight:sensorRight + thick]

    cv2.imshow('Left Frame', leftFrame)
    cv2.imshow('Right Frame', rightFrame)

    if iframe == 0:
        # บันทึกเฟรมแรกไว้เป็น baseline
        firstLeftFrame = leftFrame.copy()
        firstRightFrame = rightFrame.copy()

    if iframe > 1:
        diffLeft = np.sum(cv2.absdiff(leftFrame, firstLeftFrame))
        diffRight = np.sum(cv2.absdiff(rightFrame, firstRightFrame))
        print(diffLeft, diffRight)

    cv2.imshow('Frame', frame)
    iframe += 1

    if cv2.waitKey(1) == 32:  # Spacebar
        break

cap.release()
cv2.destroyAllWindows()
