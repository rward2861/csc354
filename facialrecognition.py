"""
  Source worked off of for code: https://www.superdatascience.com/opencv-face-recognition/
  and Team FiPi
"""
import socket
import threading
import sys, os
import cv2
import os 
import numpy as np
import time 
import matplotlib.pyplot as plt
import detect_face

subjects = ["", "Janeel", "Eric", "Steph"]


#prepare training data
def prepare_training_data(data_folder_path):
    
    #get the directories (one directory for each subject) in data folder
    dirs = os.listdir(data_folder_path)
    
    #list to hold all subject faces
    faces = []
    #list to hold labels for all subjects
    labels = []
    
    #let's go through each directory and read images within it
    for dir_name in dirs:
        
        #directory starts with 's'
        if not dir_name.startswith("s"):
            continue;
            
        #extract label number of subject from dir_name
        label = int(dir_name.replace("s", ""))
        
        #build directory path
        subject_dir_path = (data_folder_path + "/" + dir_name)
        
        #get subject names
        subject_images_names = os.listdir(subject_dir_path)
      
        for image_name in subject_images_names:
            
            #ignore system files
            if image_name.startswith("."):
                continue;
            
            #build image path
            image_path = (subject_dir_path + "/" + image_name)

            #read image
            image = cv2.imread(image_path)
            
            #display an image window to show the image
            cv2.imshow("Training on image...", cv2.resize(image, (400, 500)))
            cv2.waitKey(10)
            
            #detect face
            face, rect = detect_face.find_faces(image)

            #ignore if no faces are present
            if face is not None:
                #add face to list of faces
                faces.append(face)
                #add label for this face
                labels.append(label)
            
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    
    return faces, labels


print("Preparing data from training file...")
faces, labels = prepare_training_data("training-data")
print("Data prepared")


print("Total faces: ", len(faces))
print("Total labels: ", len(labels))

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(faces, np.array(labels))

#function to draw rectangle on image 
def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)
    
def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 255, 0), 2)


#recognize individual and draw rectangle around face
def predict(test_img):
    #make a copy of the image as we don't want to chang original image
    img = test_img.copy()
    #detect face from the image
    face, rect = detect_face.find_faces(test_img)

    #predict the image using our face recognizer 
    label, confidence = face_recognizer.predict(face)
    #get name of respective label returned by face recognizer
    label_text = subjects[label]
    
    #draw a rectangle around face detected
    draw_rectangle(img, rect)
    #draw name of predicted person
    draw_text(img, label_text, rect[0], rect[1]-5)
    
    return img


print("Predicting images...")

#load test images
test_img1 = cv2.imread("test-data/test1.jpg")
test_img2 = cv2.imread("test-data/test2.jpg")
test_img3 = cv2.imread("test-data/test3.jpg")
#perform a prediction
predicted_img1 = predict(test_img1)
predicted_img2 = predict(test_img2)
predicted_img3 = predict(test_img3)
print("Prediction complete")

#checking array to see if authorized user is present, if so, create socket and attempt connection with Raspberry Pi
while subjects[3]:
    if subjects[1] == "Janeel":
        print (subjects[1] + " is an authorized user!")
        cv2.imshow(subjects[1], cv2.resize(predicted_img1, (400, 500)))
        print ("Sending signal to Pi.. ")
        #socket communication
        ipaddress = '169.254.208.93'
        port = 35300
        IPaddr = socket.gethostbyname(ipaddress)
        message = 'READY'
        buffersize = 1024
        serverInfo = ((IPaddr, port))
        try:
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientSocket.connect(serverInfo)
            print ('Almost there..')
        except socket.error as err:
            print('Socket connection error:', err)
            sys.exit()
        try:
            clientSocket.send(message.encode())
            print('Signal sent successfully!')
        except MsgError as e:
            print('Looks like we werent able to do it.. Sorry')
        clientSocket.close() 
        break   
        
    else:
        print (subjects[1] + " is a Non-Authorized User.")
        sys.exit(0)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.destroyAllWindows()

