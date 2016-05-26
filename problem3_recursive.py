"""

Program : problem3_recursive.py
Author  : Jigar R. Gosalia
Verion  : 1.0
Course  : CSC-520 (Homework 2)
Prof.   : Srinivasan Mandyam

Write a recursive function that expects a pathname as an argument.
The pathname can be either the name of a file or the name of a directory.
If the pathname refers to a file, its name is displayed, followed by its contents.
Otherwise, if the pathname refers to a directory, the function is applied to each
name in the directory. Test this function in a new program.


NOTE:
1. Instead of printing the complete content of the file, I am printing the file
    content size so that screen doesn't fly when you are running the program.
2. Exception handling has been added to the code as isfile() returns true for images etc.
    This is to avoid abrupt termination of the program.

"""

import os

def fileContent(prefix, path):
    """ fileContent is a recursive function that expects a pathname as an agrument, if that pathname is a file
        then it prints its content size and if it is a directory, it recursively goes over all the files/folders
        under the directory and prints their content size.

        prefix - it is used to print the files and directories in a folder structure hierarchy. """
    TAB = "    "
    # Exception handling required to handle situations where isfile returns true for images
    try:
        if os.path.isfile(path):
            prefix = prefix + TAB
            file = open(path, "r")
            print(prefix + "FileName     : " + path)
            print(prefix + "Content Size : " + str(len(file.read())))
        elif os.path.isdir(path):
            prefix = prefix + TAB
            print(prefix + "-----------------------------------")
            print(prefix + "Entering directory : " + path)
            originalPath = os.getcwd()
            os.chdir(path)
            for file in os.listdir(path):
                fileContent(prefix, os.getcwd() + os.sep + file)
            os.chdir(originalPath)
            print(prefix + "Exiting directory  : " + path)
            print(prefix + "-----------------------------------")
        else:
            print(prefix + path + " is not a file or directory!")
    except Exception as exception:
        print(prefix + path + " is not readable hence can't print its content size!")

def main():
    """ Main method. """
    print("\n" * 10)
    print("Given a file name, program will recursively print the directories and file's content!", end="\n\n");
    input("Press ENTER to start execution ... \n");
    while True:
        fileName = input("Enter a valid file path (RELATIVE ONLY and NOT ABSOLUTE): ")
        if fileName != None and len(fileName) != 0 and os.path.exists(os.getcwd() + os.sep + fileName):
            fileContent("", os.getcwd() + os.sep + fileName)
            break
        else:
            print("<" + fileName + "> is not valid file path, Try again!", end="\n\n")
    
"""
    Starting point
"""
main()
