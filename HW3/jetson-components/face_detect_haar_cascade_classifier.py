#Reference- https://docs.opencv.org/3.4.1/d7/d8b/tutorial_py_face_detection.html

import numpy as np
import cv2 as cv

#load pre-trained model
face_cascade = cv.CascadeClassifier('../opencv-4.0.0/data/haarcascades/haarcascade_frontalface_default.xml')

#load test image
img = cv.imread('man.jpeg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()
