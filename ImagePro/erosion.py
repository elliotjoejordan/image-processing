'''
    Elliot Jordan
    Erosion
    Checks image exists and records size
    Takes input image to erode, cycles through each pixel and creates a 5x5 box of pixels
    Selects lowest (darkest) pixel to replace current pixel and writes to imageAlt
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

def erode(img):
    # iterate over the entire image
    for px in range(0, w):
        for py in range(0, h):
            #Insert erosion for 5x5 grid on each pixel
            #Empty list of pixels in the 5x5 area
            temp = []
            #Iterate through all pixels in 5x5
            for i in range(px-2, px+3):
                for j in range(py-2, py+3):
                    #Check that they exist in the image
                    if i >=0 and i < w:
                        if j>=0 and j< h:
                            #Add to list
                            temp.append(img[i][j])
            #Write low pixel onto alt image
            imageAlt[px][py] = min(temp)
    #Write to new image eroded
    return (imageAlt)


erode(image)
cv2.imwrite('./lena_erosion.png', imageAlt)
