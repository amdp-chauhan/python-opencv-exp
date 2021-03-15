import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os 

people = []
FACE_DIR = '../Resources/Faces/train'
haar_cascade = cv.CascadeClassifier('../Resources/data/haar-face-default.xml')

for i in os.listdir(FACE_DIR):
    people.append(i)

train_features = []
train_labels = []

# Function to create train feature and label set
def create_train():
    # Iterate over photos
    for person in people:
        # person's directory path
        photos_path = os.path.join(FACE_DIR, person)
        # init index of person 
        person_label = people.index(person)
        # iterating over person images
        for img in os.listdir(photos_path):
            # reading person's image in grey format
            img_path = os.path.join(photos_path, img)
            img_array = cv.imread(img_path)
            grey_im = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            # detecting the face in a given image
            faces_rect = haar_cascade.detectMultiScale(grey_im, scaleFactor=1.1, minNeighbors=4)
            # cropping only the face of the image, and append to the features list
            for (x, y, w, h) in faces_rect:
                faces_roi = grey_im[y:y+h, x:x+w]
                train_features.append(faces_roi)
                train_labels.append(person_label)

create_train()

# Convert train features and labels to np array
train_features_np = np.array(train_features, dtype='object')
train_labels_np = np.array(train_labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features list and labels list
face_recognizer.train(train_features_np, train_labels_np)
face_recognizer.save('trained-recognizer.yml')
np.save('train-features.npy', train_features_np)
np.save('train-labels.npy', train_labels_np)


cv.waitKey(0)