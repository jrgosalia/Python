"""
Program : problem1_navigator.py
Author  : Jigar R. Gosalia
Verion  : 1.0
Course  : CSC-520 (Homework 2)
Prof.   : Srinivasan Mandyam

Write a program that allows the user to navigate the lines of text in a file.
The program should prompt the user for a filename and input the lines of text
into a list. The program then enters a loop in which it prints the number of
lines in the file and prompts the user for a line number. Actual line numbers
range from 1 to the number of lines in the file. If the input is 0, the program
quits. Otherwise, the program prints the line associated with that number.

"""

from library import getLinesByDelimiter

def main():
    """ Main method """
    print("\n" * 10)
    print("Given a file name and list of line numbers, program prints those lines, if line number is 0 then programs quits!", end="\n\n");
    input("Press ENTER to start execution ... \n");

    logOut = False
    # To store all the lines by lineNumber for faster retrieval
    linesDictionary = {}
    # To store lines from a file delimited by \n
    lines = []
    lineNumbers = ""
    lineNumber = 1
    while (len(lines) == 0):
        fileName = input("Enter the file name (RELATIVE ONLY and NOT ABSOLUTE): ")
        print("\n\n" * 1)
        lines = getLinesByDelimiter(fileName)
    for line in lines:
        linesDictionary[lineNumber] = line
        lineNumber += 1
    while not logOut:
        lineNumbers = ""
        # Check if given list of line numbers is actual line numbers
        while (len(lineNumbers) == 0 or \
               lineNumbers.strip().replace(" ", "").isdigit() == False):
            lineNumbers = input("Enter space delimited list of line numbers ranging(1-" + str(len(lines)) + ") or enter 0 to quit: ")
        print("\n\n" * 1)
        for lineNumber in lineNumbers.strip().split():
            # Quit program when line number is 0
            if (int(lineNumber) == 0):
                logOut = True
                print("line " + str(lineNumber) + " : QUITTING PROGRAM AS INPUT IS ZERO LINENUMBER", end="\n\n")
            # Print warning if the given line number is greater then total number of lines in the file
            elif (int(lineNumber) > len(lines)):
                print("line " + str(lineNumber) + " : " + "[WARNING] Given line number " + lineNumber + " is greater then lines present in file", end="\n\n")
            # Print the valid line number
            else:
                print("line " + str(lineNumber) + " : " + str(linesDictionary.get(int(lineNumber), None)), end="\n\n")
        print("-" * 110)

"""
    Starting point
"""
main()
