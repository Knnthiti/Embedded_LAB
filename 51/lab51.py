import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # Detect object in video stream
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
SCALE_FACTOR = 1.3
MIN_NEIGHBORS = 5
count = 0 # Initialize face image counter
cap = cv2.VideoCapture(0) # Start capturing video
while True:
    _, frame = cap.read() # Capture video frame
    # 🔹 ปรับขนาดเฟรมตรงนี้
    frame = cv2.resize(frame, (150, 150))

    height, width, channels = frame.shape
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # Convert frame to grayscale

    faces = face_cascade.detectMultiScale(gray, SCALE_FACTOR, MIN_NEIGHBORS) # Detect frames of different sizes
    for (x,y,w,h) in faces: # Loop for each faces
        cv2.rectangle(frame,(x,y),(x+w,y+ h),(128,0,128),1) # Crop the image frame into rectangle
        face = frame[y:y+ h, x:x+w] # Convert Crop the image to face
        faceGray = gray[y:y+ h, x:x+w]
        
        cv2.imshow('Face', face) # Display the Face frame

        eyes = eye_cascade.detectMultiScale(faceGray) # Detect frames of different sizes
        for (ex,ey,ew,eh) in eyes: # Loop for each eyes
            cv2.rectangle(face,(ex,ey),(ex+ ew,ey+ eh),(255,0,0),1) # Crop the image frame into rectangle

            count += 1 # Increment sample face image
            filename = str(count)+ ".jpg"
            cv2.imwrite("images/E" + filename , face) # Save the eye detect to jpg file

            height2, width2, channels = face.shape           
            x1 = x - int(width2/4)
            if x1<1:
                x1=1
            x2 = x+w + int(width2/4)
            if x2>width:
                x2=width
            y1 = y - int(height2/4)
            if y1<1:
                y1=1
            y2 = y+h + int(height2/4)
            if y2>height:
                y2=height
                
            cv2.imwrite("images\F"+filename , frame[y1 :y2, x1: x2])   # Save the face image to jpg file

        smile = smile_cascade.detectMultiScale(faceGray) # Detect frames of different sizes
        for (sx,sy,sw,sh) in smile: # Loop for each smile
            cv2.rectangle(face,(sx,sy),(sx+sw,sy+sh),(0,128,0),1) # Crop the image frame into rectangle

    cv2.putText(frame, str(count), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    cv2.putText(frame, str(width)+'x'+str(height), (10, height-20), cv2.FONT_HERSHEY_SIMPLEX, .6, (0, 255, 255), 1)

    cv2.imshow('Frame', frame) # Display the video frame
    if cv2.waitKey(1) == 32: # if the spacebar key is pressed, break from the loop
        break
    elif count>= 100: # If image taken reach 100, stop taking video
        break

cap.release() # cleanup the camera
cv2.destroyAllWindows() # close any open windows