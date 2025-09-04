import cv2
import datetime
import imutils
cap = cv2.VideoCapture(0) # initialize the camera
startTime = datetime.datetime.now() # start time
firstFrame = None # initialize the first frame in the video stream
motionCounter = 0
while True: # loop over the frames of the video
    timestamp = datetime.datetime.now() # update the timestamp
    ret, frame = cap.read() # reading from webcam
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Converting color image to gray scale image
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    if firstFrame is None: # if the first frame is None, initialize it
        firstFrame = gray
        continue
    diff_frame = cv2.absdiff(firstFrame, gray) # difference between the current frame and first frame

    thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1] # greater than 30 show white color
    thresh_frame = cv2.dilate(thresh_frame, None, iterations= 2) # dilate the thresholded image to fill in holes
    (cnts, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, cnts, -1, (255, 0, 0), 2) # draw all contours on the frame

    for contour in cnts: # loop over the contours
        if cv2.contourArea(contour) < 3000: # if the contour is too small, ignore it
            continue
        (x, y, w, h) = cv2.boundingRect(contour) # compute the bounding box for the contour
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1) # draw box on the frame
        motionCounter += 1

    ts = timestamp.strftime("%d %b %Y %I:%M:%S%p") # draw timestamp on the frame
    cv2.putText(frame, " {} ".format(ts), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)

    if (timestamp - startTime).seconds >= 10 : # if enough time has passed between uploads
        if motionCounter >= 3: # number of frames with consistent motion is high enough
            print(format(ts) , ' , motion = ', motionCounter , " , time = ", (timestamp - startTime).seconds)
            cv2.imwrite('capture1.png', frame) # write the image to png file
            startTime = timestamp # update the last uploaded timestamp
            motionCounter = 0

    filename = "P" + timestamp.strftime("%Y%m%d-%H%M%S") + ".jpg"
    cv2.imwrite(filename , frame) # write the image to jpg file

    height, width, channels = frame.shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    filenameV = "V" + timestamp.strftime("%Y%m%d-%H%M%S") + ".mp4"
    video = cv2.VideoWriter(filenameV, fourcc, 20, (width, height))
    for i in range(200): # Record 10 Sec
        ret, frame = cap.read() # reading from webcam
        video.write(frame) # write the video to mp4 file
    video.release()

    cv2.imshow("Difference Frame", diff_frame)
    cv2.imshow("Threshhold Frame", thresh_frame)
    cv2.imshow("GaussianBlur Gray Frame", gray) # show the frame
    cv2.imshow("Color Frame", frame)
    if cv2.waitKey(1) == 32: # spacebar key is pressed, break from the loop
        break
cap.release() # cleanup the camera
cv2.destroyAllWindows() # close any open windows