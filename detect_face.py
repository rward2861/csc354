"""
  Source worked off of for code: https://www.superdatascience.com/opencv-face-recognition/
  and Team FiPi
"""
import cv2

#function to detect face using OpenCV
def find_faces(img):
    #convert the test image to gray image as opencv face detector expects gray images
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #load OpenCV face detector
    face_cascade = cv2.CascadeClassifier('opencv/sources/data/lbpcascades/lbpcascade_frontalface.xml')

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
    
    #if no faces are detected then return original img
    if (len(faces) == 0):
        return None, None
 
    (x, y, w, h) = faces[0]
    
    #return only the face part of the image
    return (gray[y:y+w, x:x+h], faces[0])
