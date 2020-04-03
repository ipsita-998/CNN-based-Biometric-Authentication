# CNN BASED BIOMETRIC AUTHENTICATION 

## INTRODUCTION

This project involves the implementation of identification of an individual by facial recognition 
using fuzzy Convolution Neural Networks.


### What is Biometrics??
THE IDENTIFICATION OF INDIVIDUALS BY DISTINCT AND INVARIANT PHYSIOLOGICAL CHARACTERISTICS IS KNOWN AS BIOMETRICS.


 #### BIOMETRICS Types :
- UNIMODAL –SINGLE MODALITY/ FEATURE(it can be either face ,iris, finger-vein, fingerprint, etc)
- MULTIMODAL -MULTIPLE FEATURES OR DIFFERENT INSTANCES OF THE SAME FEATURES


### CONVOLUTION NEURAL NETWORKS
- The name “convolutional neural network” indicates that the network employs a mathematical operation called convolution.

- Convolutional networks are simply neural networks that use convolution in place of general matrix multiplication in at least one of their layers.



## DEPENDENCIES


-jupyter notebook / google collaboratory
- SDUMLA-HMT DATABASE

 ## CREATING THE FACIAL DATABASE

- the database can be dowloded from the below link or any relevant facial dataset can be used.
- http://mla.sdu.edu.cn/info/1006/1195.htm
- more information on the dataset can be found in the link below
 https://link.springer.com/chapter/10.1007/978-3-642-25449-9_33
- You can also use the dataset provided in this repository
- if your dataset is small you can increase the size of the dataset by image augmentations the code for which is availalble in the file generation.py

## STEPS OF IMPLEMENTATION


- Loading the dataset and creating categorical labels corresponding to the image.
- Converting RGB to GreyScale........(as the number of trainable parameters will be less and the training time will reduce).
- Dividing the pixel by 255 it is extremely important for each feature to have a similar range such that our gradients don't explode during backpropogation.
- ONE HOT ENCODING
- Initialising the CNN model
- Training the model with and without dropout
- Validation and prediction with the trained model


## EXECUTION
- Set the path to the database and execute the code.
