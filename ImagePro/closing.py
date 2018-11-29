'''
    Elliot Jordan
    CLosing
    imports dilate and erode methods from dilation.py and erosion.py to combine for closing

'''


import numpy as np
import cv2
import sys

#Must read initial image (pixels for reference) and alt image (written onto)
image = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
imageAlt = cv2.imread(sys.argv[2], cv2.IMREAD_GRAYSCALE)

# check if it has loaded
if not image is None:
    # get image properties width and height
    h, w = np.shape(image)
else:
    print("No image file successfully loaded.")

from dilation import dilate
from erosion import erode
# Imports the functions which make up closing

def closing():

    cv2.imwrite('./lena_closing.png', erode(dilate(image)))
    # As closing is dilation followed by erosion,
    #  uses the functions embedded within each other on the original image to output as altered image

closing()
# Calls closing function (after defined)