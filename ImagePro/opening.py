'''
    Elliot Jordan
    Opening
    imports dilate and erode methods from dilation.py and erosion.py to combine for opening

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

# Imports functions form erosion and dilation to make up the functionality of opening
from dilation import dilate
from erosion import erode

def opening():

    cv2.imwrite('./lena_opening.png', dilate(erode(image)))
    # Calls functions inside each other to create opening and writes to altered file

opening()
# Calls opening function after it is defined