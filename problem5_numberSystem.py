"""
Program : problem5_numberSystem.py
Author  : Jigar R. Gosalia
Verion  : 1.0
Course  : CSC-520 (Homework 1)
Prof.   : Srinivasan Mandyam

Write a program that reads the input from the keyboard and converts into another number system as shown below
(a) 3 digit Decimal to Octal
(b) 3 digit Decimal to Binary
(c) 3 digit Decimal to Hexadecimal
"""

from problem5_library import dec2oct, dec2bin, dec2hex;

# Constants
OCTAL_OPTION = 1;
BINARY_OPTION = 2;
HEXADECIMAL_OPTION = 3;
EXIT_OPTION = 4;

print("Welcome to Number Conversion System!", end="\n\n");

print("Enter Decimal Number(>=0) & Choose the Number System(1-3) to convert decimal number.", end="\n\n");

input("Press ENTER to start execution ... \n");

while (True):
    # Keep checking with user until user enters valid decimal number (>=0).
    while (True):
        decimalInput = input("Enter Decimal number (>=0) to convert: ");
        if (decimalInput == "" or "." in decimalInput or int(decimalInput) < 0):
            print("Invalid decimal number, try again!", end="\n\n");
        else:
            decimal = int(decimalInput);
            break;
    # Keep checking with user until user chooses valid number system.
    while (True):
        systemInput = input("Choose Number System \n1. Octal \n2. Binary \n3. Hexadecimal \n4. Exit \n-> ");
        if (systemInput == "" or "." in systemInput or int(systemInput) <= 0 or int(systemInput) > 4):
            print("Invalid option, choose again!", end="\n\n");
        else:
            system = int(systemInput);
            break;
    # Depending on number system selected display the equivalent of decimal number.
    if (system == OCTAL_OPTION):
        print("Decimal(%d) -> Octal(%s)" % (decimal, dec2oct(decimal)), end="\n\n");
    elif (system == BINARY_OPTION):
        print("Decimal(%d) -> Binary(%s)" % (decimal, dec2bin(decimal)), end="\n\n");
    elif (system == HEXADECIMAL_OPTION):
        print("Decimal(%d) -> Hexadecimal(%s)" % (decimal, dec2hex(decimal)), end="\n\n");
    elif (system == EXIT_OPTION):
        print("Exiting execution ... ", end="\n\n");
        break;

input("Press ENTER to exit ... \n");
