"""
Program : problem2_km2miles.py
Author  : Jigar R. Gosalia
Verion  : 1.0
Course  : CSC-520 (Homework 1)
Prof.   : Srinivasan Mandyam

Write a program that takes Kilometers as input and produces corresponding number of nautical miles. 

Reference links: Conversion factor from http://www.metric-conversions.org/length/kilometers-to-us-nautical-miles-table.htm
"""

# Conversion Factor from kilometers to miles.
# 1 km = 0.53996 nautical miles
CONVERSION_FACTOR = 0.53996;

print("Convert kilometers into nautical miles.\n");

input("Press ENTER to start execution ... \n");

# Get kilometers for conversion.
while(True):
    value = input("Enter kilometers to convert into nautical miles: ");
    # Kilometers can't be negative number. 
    if (value == "" or float(value) < 0):
        print("Invalid KILOMETERS, try again!", end="\n\n");
    else:
        kilometers = float(value);
        break;

miles = kilometers * CONVERSION_FACTOR;

print("\n");

print("%.2f Kilometers is equivalent to %.2f Nautical Miles." % (kilometers, miles), end="\n\n");

input("Press ENTER to exit ... \n");
