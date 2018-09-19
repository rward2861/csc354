"""Aspects of Facial Recognition:
  1) Facial Detection
  2) Data Gathering (extracting unique characteristics that can be used to differentiate one person from another)
  3) Data Comparison (comparing of unique features, despite variations in light, angle, ect.)
  4) Face Recognition
  Source: https://www.superdatascience.com/opencv-face-recognition/
  
  Aspects of OpenCV Face Recognition:
  1) Data Gathering: Gather face data (face images in this case) of the persons you want to identify.
  2) Train the Recognizer: Feed that face data and respective names of each face to the recognizer so that it can learn.
  3) Recognition: Feed new faces of that people and see if the face recognizer you just trained recognizes them.
  
  Using: EigenFaces – cv2.face.createEigenFaceRecognizer()
  Why? 
    - algorithm understands that not all parts of the face are equally important or useful in facial recognition 
    - distinct features are most important (eyes, nose, cheeks, forehead) that have areas of MAXIMUM change 
    - looks at images of people as a whole and tries to extract the components which are relevant, while discarding the rest
"""
import cv2
import os 
import numpy as np

subjects = ["", "Janeel", "Eric", "Misc"]


#function to detect face using OpenCV
def detect_face(img):
#convert the test image to gray scale as opencv face detector expects gray images
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
#load OpenCV face detector, I am using LBP which is fast
#there is also a more accurate but slow: Haar classifier
  face_cascade = cv2.CascadeClassifier('opencv-files/lbpcascade_frontalface.xml')
 
#let's detect multiscale images(some images may be closer to camera than others)
#result is a list of faces
  faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
 
#if no faces are detected then return original img
  if (len(faces) == 0):
    return None, None
 
#under the assumption that there will be only one face,
#extract the face area
  (x, y, w, h) = faces[0]
 
#return only the face part of the image
  return gray[y:y+w, x:x+h], faces[0]

def prepare_training_data(data_folder_path):
 
#------STEP-1--------
#get the directories (one directory for each subject) in data folder
  dirs = os.listdir(data_folder_path)
 
#list to hold all subject faces
  faces = []
#list to hold labels for all subjects
  labels = []
 
#let's go through each directory and read images within it
  for dir_name in dirs:
 
#our subject directories start with letter 's' so
#ignore any non-relevant directories if any
    if not dir_name.startswith("s"):
      continue;
 
#------STEP-2--------
#extract label number of subject from dir_name
#format of dir name = slabel
#, so removing letter 's' from dir_name will give us label
label = int(dir_name.replace("s", ""))
 
#build path of directory containing images for current subject subject
#sample subject_dir_path = "training-data/s1"
subject_dir_path = data_folder_path + "/" + dir_name
 
#get the images names that are inside the given subject directory
subject_images_names = os.listdir(subject_dir_path)

#------STEP-3--------
#go through each image name, read image, 
#detect face and add face to list of faces
for image_name in subject_images_names:
 
#ignore system files like .DS_Store
  if image_name.startswith("."):
    continue;
 
#build image path
#sample image path = training-data/s1/1.pgm
image_path = subject_dir_path + "/" + image_name
 
#read image
image = cv2.imread(image_path)
 
#display an image window to show the image 
cv2.imshow("Training on image...", image)
cv2.waitKey(100)
 
#detect face
face, rect = detect_face(image)
 
#------STEP-4--------
#for the purpose of this tutorial
#we will ignore faces that are not detected
if face is not None:
#add face to list of faces
  faces.append(face)
#add label for this face
  labels.append(label)
 
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.destroyAllWindows()
 
return faces, labels

#data will be in two lists of same size
#one list will contain all the faces
#and the other list will contain respective labels for each face
print("Preparing data...")
faces, labels = prepare_training_data("training-data")
print("Data prepared")
 
#print total faces and labels
print("Total faces: ", len(faces))
print("Total labels: ", len(labels))

face_recognizer = cv2.face.createEigenFaceRecognizer()

face_recognizer.train(faces, np.array(labels))

def draw_rectangle(img, rect):
 (x, y, w, h) = rect
 cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
 
#function to draw text on give image starting from
#passed (x, y) coordinates. 
def draw_text(img, text, x, y):
 cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
 
#this function recognizes the person in image passed
#and draws a rectangle around detected face with name of the 
#subject
def predict(test_img):
#make a copy of the image as we don't want to change original image
  img = test_img.copy()
#detect face from the image
  face, rect = detect_face(img)
 
#predict the image using our face recognizer 
  label= face_recognizer.predict(face)
#get name of respective label returned by face recognizer
  label_text = subjects[label]
 
#draw a rectangle around face detected
  draw_rectangle(img, rect)
#draw name of predicted person
  draw_text(img, label_text, rect[0], rect[1]-5)
 
return img

#load test images
test_img1 = cv2.imread("test-data/test1.jpg")
test_img2 = cv2.imread("test-data/test2.jpg")
 
#perform a prediction
predicted_img1 = predict(test_img1)
predicted_img2 = predict(test_img2)
print("Prediction complete")
 
#display both images
cv2.imshow(subjects[1], predicted_img1)
cv2.imshow(subjects[2], predicted_img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
