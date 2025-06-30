# -*- coding: utf-8 -*-
# MLP for Pima Indians Dataset Serialize to JSON and HDF5
import numpy as np
from keras.preprocessing import image
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import os
import cv2

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

#label=['aneurysms','hemorrhages','normal']

def classify(img_file):
    img_name = img_file
    test_image = image.load_img(img_name, target_size = (128,128))

    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = loaded_model.predict(test_image)
    a=np.round(result[0][0])
    b=np.round(result[0][1])
    c=np.round(result[0][2])
    d=np.round(result[0][3])
    e=np.round(result[0][4])

    print(a)
    print(b)
    print(c)
    print(d)
    
    
    if a == 1:
        prediction = 'Chicken_fry'
        print(prediction)
        img = cv2.imread(img_name)
        cv2.imshow("Chicken_fry",img)
        print(prediction,img_name)


    elif b == 1:
        prediction = 'Crab_gravy'
        print(prediction)
        img = cv2.imread(img_name)
        cv2.imshow("Crab_gravy",img)
        print(prediction,img_name)

    elif c == 1:
        prediction = 'Fish_fry'
        print(prediction)
        img = cv2.imread(img_name)
        cv2.imshow("Fish_fry",img)
        print(prediction,img_name)

    elif d == 1:
        prediction = 'Mutton_briyani'
        print(prediction)
        img = cv2.imread(img_name)
        cv2.imshow("Mutton_briyani",img)
        print(prediction,img_name)
        
    elif e == 1:
        prediction = 'Prawn_fry'
        print(prediction)
        img = cv2.imread(img_name)
        cv2.imshow("Prawn_fry",img)
        print(prediction,img_name)


   
    

##test_image = image.img_to_array(test_image)
##test_image = np.expand_dims(test_image, axis = 0)
##result = loaded_model.predict(test_image)
##print(result)
##fresult=np.max(result)
##label2=label[result.argmax()]
###print(label2)


import os
path = 'data/test'
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
   for file in f:
     if '.jpg' in file:
       files.append(os.path.join(r, file))

for f in files:
   classify(f)
   print('\n')
