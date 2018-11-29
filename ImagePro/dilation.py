'''
    Elliot Jordan
    Dilation
    Checks image exists and records size
    Takes input image to dilate, cycles through each pixel and creates a 5x5 box of pixels
    Selects highest (lightest) pixel to replace current pixel and writes to imageAlt
    Writes new image to png file
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

def dilate(img):
    # iterate over the entire image
    for px in range(0, w):
        for py in range(0, h):
            #insert Dilation for 5x5 grid on each pixel
            #empty list created each time of neighbours
            temp = []
            #create 5x5 box from current pixel
            for i in range(px-2, px+3):
                for j in range(py-2, py+3):
                    #check pixel is within image range
                    if i >=0 and i < w:
                        if j>=0 and j< h:
                            #create list of pixels in 5x5
                            temp.append(img[i][j])
            #Set altered pixel to greatest (lightest) of nearby pixels
            imageAlt[px][py] = max(temp)
    #Write image to dilated image location

    return (imageAlt)


dilate(image)
cv2.imwrite('./lena_dilation.png', imageAlt)