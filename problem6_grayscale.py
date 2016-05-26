"""
Program : problem6_grayscale.py
Author  : Jigar R. Gosalia
Verion  : 1.0
Course  : CSC-520 (Homework 2)
Prof.   : Srinivasan Mandyam

Define a second version of the grayscale function that uses the allegedly crude method
of simply averaging each RGB value. Test the function by comparing its results with
those of the other version discussed in this chapter.

"""

import os
from PIL import Image
from library import *

def grayScaleStandard(image):
    """ Standard grayscale from the reference book. """
    for y in range(image.height):
        for x in range(image.width):
            (r, g, b) = image.getpixel((x, y))
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            image.putpixel((x, y), (lum, lum, lum))

def grayScaleAveragingRGB(image):
    """ Crude grayscale by averaging each value of RGB. """
    for y in range(image.height):
        for x in range(image.width):
            (r, g, b) = image.getpixel((x, y))
            avg = int((r + g + b)/3)
            image.putpixel((x, y), (avg, avg, avg))

def main():
    """ Main Method. """
    print("\n" * 10)
    print("GrayScale given image using 2 different approaches and compare them side-by-side!", end="\n\n");
    input("Press ENTER to start execution ... \n");

    fileName = input("Enter valid image file path (RELATIVE ONLY and NOT ABSOLUTE): ")
    while not validImageFile(os.getcwd() + os.sep + fileName):
        fileName = input("Enter valid image file path (RELATIVE ONLY and NOT ABSOLUTE): ")

    image = Image.open(fileName)
    print("Close the image window to continue.")
    image.show()

    (width, height) = image.size

    # Use the standard grayscale method from reference book
    newStandardImage = image.copy()
    grayScaleStandard(newStandardImage)

    # Use crude averaging RGB value method
    newImage = image.copy()
    grayScaleAveragingRGB(newImage)

    # Resulting image will be double width of original image as
    # 2 images will be placed side by side for comparison
    result = Image.new("RGB", ((2 * width + 75), (height + 50)))

    # set background to RED
    paintBackground(result, (255, 0, 0))

    # Compare the result of both the grayscale functions
    # by placing them side-by-side
    result.paste(im=newStandardImage, box=(25, 25))
    result.paste(im=newImage, box = ((width + 50), 25))

    print("Close the image window to quit.")
    result.show()

"""
    Starting point
"""
main()
