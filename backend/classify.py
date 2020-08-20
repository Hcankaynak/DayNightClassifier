import numpy as np
import matplotlib.image as mpimg
import cv2

def averageBrightness(image):
    # convert RGB to HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    sum_value_channel = np.sum(hsv_image[:,:,2])
    img_area = 600*1100
    return sum_value_channel/img_area

## Standardize the input images
def standardize_output(image):
    return cv2.resize(image,(1100,600))

def classify(image):
    
    avg = averageBrightness(image)
    predicted_label = 0 #default
    threshold = 100.0 #arbitrarily
    if(avg > threshold):
        predicted_label=1
    return predicted_label

def classifyImage(image):
    img = mpimg.imread(image)
    return classify(standardize_output(img))


