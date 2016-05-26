"""
Program : problem5_library.py
Author  : Jigar R. Gosalia
Verion  : 1.0
Course  : CSC-520 (Homework 1)
Prof.   : Srinivasan Mandyam
"""

"""
Converts given decimal number into its binary equivalent.

Args:
    decimal (int) : Decimal Number.

Returns:
    binary (str) : Binary representation of given Decimal number.
"""
def dec2bin(decimal):
    if (decimal == 0):
        return "0";
    binary = "";
    while (decimal != 0):
        remainder = decimal % 2;
        binary = str(remainder) + binary;
        decimal = decimal // 2;
    return binary;

"""
Converts given decimal number into its octal equivalent.

Args:
    decimal (int) : Decimal Number.

Returns:
    octal (str) : Octal representation of given Decimal number.
"""
def dec2oct(decimal):
    if (decimal == 0):
        return "0";
    octal = "";
    while (decimal != 0):
        remainder = decimal % 8;
        octal = str(remainder) + octal;
        decimal = decimal // 8;
    return octal;

"""
Converts given decimal number into its hexadecimal equivalent.

Args:
    decimal (int) : Decimal Number.

Returns:
    hexadecimal (str) : Hexadecimal representation of given Decimal number.
"""
def dec2hex(decimal):
    if (decimal == 0):
        return "0";
    hexadecimal = "";
    while (decimal != 0):
        remainder = decimal % 16;
        hexadecimal = getHexValue(remainder) + hexadecimal;
        decimal = decimal // 16;
    return hexadecimal;

"""
Get Hexadecimal character for given Decimal Number.

Args:
    decimal (int) : Decimal Number (0-15).

Returns:
    hexValue (str) : Hex character of given Decimal number.
"""
def getHexValue(decimal):
    if (decimal <= 9):
        return str(decimal);
    elif (decimal == 10):
        return 'A';
    elif (decimal == 11):
        return 'B';
    elif (decimal == 12):
        return 'C';
    elif (decimal == 13):
        return 'D';
    elif (decimal == 14):
        return 'E';
    else:
        return 'F';

