"""
Program : library.py
Author  : Jigar R. Gosalia
Verion  : 1.0
Course  : CSC-520 (Homework 2)
Prof.   : Srinivasan Mandyam

library to hold common functions.

"""
import os

imageFileExtensions = ['pdf', 'bmp', 'jpg', 'svg',
                       'pcx', 'ico', 'gif', 'png',
                       'pict', 'jpeg', 'tiff']

def getLinesByDelimiter(fileName):
    """ getLinesByDelimiter validates the given fileName.

        Returns all lines present in a valid file. """
    lines = []
    if (fileName != None and len(fileName) > 0 and os.path.exists(fileName)):
        if os.path.isfile(fileName):
            file = open(fileName, 'r')
            lines = file.read().split("\n")
            if (len(lines) > 0):
                return lines
            else:
                print("<" + fileName + "> is an empty file!", end="\n\n")
        else:
            print("<" + fileName + "> is not a file!", end="\n\n")
    else:
        print("<" + fileName + "> doesn't exists, try again!", end="\n\n")
    return lines

def getLines(fileName):
    """ getLines validates the given fileName.

        Returns all lines present in a valid file. """
    lines = ""
    if (fileName != None and len(fileName) > 0 and os.path.exists(fileName)):
        if os.path.isfile(fileName):
            file = open(fileName, 'r')
            lines = file.read()
            if (len(lines) > 0):
                return lines
            else:
                print("<" + fileName + "> is an empty file!", end="\n\n")
        else:
            print("<" + fileName + "> is not a file!", end="\n\n")
    else:
        print("<" + fileName + "> doesn't exists, try again!", end="\n\n")
    return lines

def validImageFile(fileName):
    """ Check if the given file is a valid image file. """
    if (fileName != None and len(fileName) > 0 and os.path.exists(fileName)):
        extn = fileName.split(".")[-1]
        if os.path.isfile(fileName) and extn != "" and extn in imageFileExtensions:
            return True
        else:
            print("<" + fileName + "> is not a valid Image file!", end="\n\n")
    else:
        print("<" + fileName + "> doesn't exists!", end="\n\n")
    return False

def validInt(value):
    """ Check if the given value is valid RGB value [0-255]. """
    if (value != None and len(value) > 0 and value.isdigit()):
        if (int(value) >= 0 and int(value) <= 255):
            return True
        else:
            print("<" + value + "> is not a valid RGB value[0-255]!", end="\n\n")
    else:
        print("<" + value + "> is not a number!", end="\n\n")
    return False

def paintBackground(image, rgbTuple):
    """ Paint image's background with given RGB tuple. """
    for x in range(image.width):
        for y in range(image.height):
            image.putpixel((x, y), rgbTuple)
