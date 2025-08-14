import cv2
import numpy
cap = cv2.VideoCapture("http://192.168.25.150:4747/video") # initialize the camera
while True:
    ret, frame = cap.read() # reading from webcam
    cv2.imshow('Frame BGR',frame) # show the frame BGR
    if cv2.waitKey(1) == 32: # check press spacebar
        break

cap.release() # cleanup the camera
cv2.destroyAllWindows()