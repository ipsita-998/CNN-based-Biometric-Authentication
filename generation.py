#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 22:37:06 2019

@author: ipsita
"""
import cv2
import numpy as np
# load the input image (whose path was supplied via command line
# argument) and display the image to our screen
image = cv2.imread('A2.bmp')
#cv2.imshow("Image", image)
#cv2.waitKey(0)
(h, w, d) = image.shape

crop = image[30:h, 10:w]
resizecrop = cv2.resize(crop,(240,320))
cv2.imwrite('messigray11.png',resizecrop)

translation_matrix = np.float32([ [1,0,70], [0,1,110] ])
img_translation = cv2.warpAffine(image, translation_matrix, (h + 70, w + 110))
cv2.imwrite('messigray.png',img_translation)

resized1 = cv2.resize(image, (200, 200))
resized = cv2.resize(resized1,(240,320))

#rotation
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0) #-45 for clockwise
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("OpenCV Rotation", rotated)
cv2.waitKey(0)

cv2.imshow("img_translation", img_translation)
cv2.waitKey(0)

#save image

cv2.imwrite('messigray.png',image)

#cv2.destroyAllWindows() #to close all the display windows

import os
for k in range(10):
    L=k+1
    a=['AF','BF','CF','DF','EF','FF','GF','HF','IF','JF']
    dire='/Users/ipsita/Desktop/fv_dataset/00'+str(L)
    os.chdir(dire)
    print(os.getcwd(),a[k],L)
    j=78 #J=6,30,54,78 FOR CONSECUTIVE 4 ITERATIONS TO GENERATE 102 IMAGES WHICH INCLUDES THE ORIGINAL 6 IMAGES ALSO
    for i in range(6):
            
            im=a[k]+str(i+1)+'.bmp'
            #print(im)
            image=cv2.imread(im)
            (h, w, d) = image.shape
            
            crop = image[2:h, 10:w]
            resizecrop = cv2.resize(crop,(240,320))
            j=j+1
            name=a[k]+str(j)+'.bmp'
            cv2.imwrite(name,resizecrop)
            
            translation_matrix = np.float32([ [1,0,15], [0,1,14] ])
            img_translation = cv2.warpAffine(image, translation_matrix, (h + 15, w + 14))
            j=j+1
            name=a[k]+str(j)+'.bmp'
            cv2.imwrite(name,img_translation)
            
            resized1 = cv2.resize(image, (110, 140))
            resized = cv2.resize(resized1,(240,320))
            j=j+1
            name=a[k]+str(j)+'.bmp'
            cv2.imwrite(name,resized)
            
            center = (w // 2, h // 2)
            M = cv2.getRotationMatrix2D(center,-5, 1.0) #-45 for clockwise
            rotated = cv2.warpAffine(image, M, (w, h))
            j=j+1
            name=a[k]+str(j)+'.bmp'
            cv2.imwrite(name,rotated)
#*******************************************************#           
#to access the face dataset in google collab run it line by line           
imagename = []       
lis=['A','B','C','D','E','F','G','H','I','J']           
for images in os.listdir('/content/drive/My Drive/FACE_DATABASE'): #lisdir used to make the list of paths 
    print(images)
    imagename.append(images)
    
del imagename[0] #if ds_store not there then remove this
imagename.sort()
#print(imagename)

for im in lis:
    for i in range(1,85):
        namedir='/content/drive/My Drive/FACE_DATABASE'+'/'+imagename[i]+im+str(i)
        print(namedir)
      
    #imagee=cv2.imread(namedir)
        
        
    
   

