import numpy as np
import matplotlib.image as mpimg
import cv2

# find the average brightness
def averageBrightness(image):
    # convert RGB to HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    sum_value_channel = np.sum(hsv_image[:,:,2])
    # this is standarized value for all input images.
    img_area = 600*1100
    # return the density of calculated values
    return sum_value_channel/img_area

## Standardize the input images
def standardize_output(image):
    # resize input image to 1100x600
    return cv2.resize(image,(1100,600))
# For classifying image
def classify(image):
    # getting avg value
    avg = averageBrightness(image)
    # default value for prediction 
    # 0 is night 
    # 1 is day
    predicted_label = 0 
    threshold = 100.0 # threshold for avg brightness
    # if avg higher than threshold 
    if(avg > threshold):
        # assign predicted value as day
        predicted_label=1
    # if not higher set as default night
    return predicted_label

# helper function for classify
def classifyImage(image):
    # open image with imread
    img = mpimg.imread(image)
    # standardize image and send it to classify
    return classify(standardize_output(img))


