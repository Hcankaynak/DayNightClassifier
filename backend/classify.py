import numpy as np

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import os
import glob # library for loading images from a directory





def load_dataset(image_dir):
    
    # Populate this empty image list
    im_list = []
    image_types = ["day", "night"]
    
    # Iterate through each color folder
    for im_type in image_types:
        
        # Iterate through each image file in each image_type folder
        # glob reads in any image with the extension "image_dir/im_type/*"
        for file in glob.glob(os.path.join(image_dir, im_type, "*")):
            
            # Read in the image
            im = mpimg.imread(file)
            
            # Check if the image exists/if it's been correctly read-in
            if not im is None:
                # Append the image, and it's type (red, green, yellow) to the image list
                im_list.append((im, im_type))
    
    return im_list

image_dir_training = "./day_night_images/training"
image_dir_test = "./day_night_images/test"
IMAGE_LIST = load_dataset(image_dir_training)



# Select an image and its label by list index
image_index = 0
selected_image = IMAGE_LIST[image_index][0]
selected_label = IMAGE_LIST[image_index][1]
print("SHAPE:",selected_image.shape,"\nLABEL:", selected_label)

def avg_brightness(image):
    # convert RGB to HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    sum_value_channel = np.sum(hsv_image[:,:,2])
    img_area = 600*1100
    return sum_value_channel/img_area

## Standardize the input images
def standardize_output(image):
    return cv2.resize(image,(1100,600))


## Encode the images, by assigning 0/1 to night/day
def encode(label):
    if label=='night':
        return 0
    return 1

## Generate a standardized list of images
# Input : image-label pairs
# Output: list of **standardized** images which are of same size and have numerical labels attached
def standardize(image_list):
    output = []
    for i in image_list:
        image , label = i[0], i[1]
        output.append((standardize_output(image), encode(label)))
    return output

## Standardize images by invoking the above functions on real data
STANDARDIZED_LIST = standardize(IMAGE_LIST)



f, (ax1, ax2) = plt.subplots(1, 2, figsize=(16,8))

ax1.imshow(STANDARDIZED_LIST[1][0])
ax1.set_title(STANDARDIZED_LIST[1][1])

ax2.imshow(STANDARDIZED_LIST[234][0])
ax2.set_title(STANDARDIZED_LIST[234][1])


def classify(image):
    
    avg = avg_brightness(image)
    predicted_label = 0 #default
    threshold = 30.0 #arbitrarily
    if(avg > threshold):
        predicted_label=1
    return predicted_label


import random
TEST_IMAGE_LIST = load_dataset(image_dir_test)
STANDARDIZED_TEST_LIST = standardize(TEST_IMAGE_LIST)
random.shuffle(STANDARDIZED_TEST_LIST)


def misclassified_images(test_images):
    misclass=[]
    for i in test_images:
        img,true_label=i[0],i[1]
        predicted_label=classify(img)
        if(predicted_label!=true_label):
            misclass.append((img,predicted_label))
    return misclass


total = len(STANDARDIZED_TEST_LIST)
wrong = len(misclassified_images(STANDARDIZED_TEST_LIST))
correct = total - wrong
print("ACCURACY = ", correct/total)
print("NUMBER OF MISCLASSIFIED IMAGES = ",wrong)
print("TOTAL IMAGES = ",total)



f, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(20,10))
MISCLASSIFIED = misclassified_images(STANDARDIZED_TEST_LIST)
ax1.imshow(MISCLASSIFIED[0][0])
ax1.set_title(MISCLASSIFIED[0][1])
ax2.imshow(MISCLASSIFIED[3][0])
ax2.set_title(MISCLASSIFIED[3][1])
ax3.imshow(MISCLASSIFIED[2][0])
ax3.set_title(MISCLASSIFIED[2][1])
ax4.imshow(MISCLASSIFIED[11][0])
ax4.set_title(MISCLASSIFIED[11][1])
print("Predicted Label = Night : 0, Day : 1")