"""
Program : problem5_posterize.py
Author  : Jigar R. Gosalia
Verion  : 1.0
Course  : CSC-520 (Homework 2)
Prof.   : Srinivasan Mandyam

Define and test a function named posterize.
This function expects an image and a tuple of RGB values as arguments.
The function modifies the image like the blackAndWhite function, but
uses the given RGB values instead of black.

"""

import os
from PIL import Image
from library import validImageFile
from library import validInt

def blackAndWhite(rgbTuple, image):
    """ Converts the image to black and white from given RGB value. """
    whitePixel = (255, 255, 255)
    for y in range(image.height):
        for x in range(image.width):
            (r, g, b) = image.getpixel((x, y))
            average = (r + g + b)/3
            if average < 128:
                image.putpixel((x, y), rgbTuple)
            else:
                image.putpixel((x, y), whitePixel)

def main():
    """ Main Method. """
    print("\n" * 10)
    print("Posterize given image from given RGB value to black and white", end="\n\n");
    input("Press ENTER to start execution ... \n");

    fileName = input("Enter valid image file path (RELATIVE ONLY and NOT ABSOLUTE): ")
    while not validImageFile(os.getcwd() + os.sep + fileName):
        fileName = input("Enter valid image file path (RELATIVE ONLY and NOT ABSOLUTE): ")

    red = input("Enter value of RED[0-255] in RGB: ")
    while not validInt(red):
        red = input("Enter value of RED[0-255] in RGB: ")

    green = input("Enter value of GREEN[0-255] in RGB: ")
    while not validInt(green):
        green = input("Enter value of GREEN[0-255] in RGB: ")

    blue = input("Enter value of BLUE[0-255] in RGB: ")
    while not validInt(blue):
        blue = input("Enter value of BLUE[0-255] in RGB: ")

    rgbTuple = (int(red), int(green), int(blue))

    image = Image.open(fileName)
    print("Close the image window to continue.")
    image.show()

    blackAndWhite(rgbTuple, image)
    print("Close the image window to quit.")
    image.show()

"""
    Starting point
"""
main()
