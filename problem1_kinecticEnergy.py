"""
Program : problem1_kinecticEnergy.py
Author  : Jigar R. Gosalia
Verion  : 1.0
Course  : CSC-520 (Homework 1)
Prof.   : Srinivasan Mandyam

The kinetic energy of a moving object is given by the formula

    KE=(1/2)mv**2

Where m is object’s mass and v is the velocity.

Write a program that reads the input values from the KB and display the KE of an object in Joules.
"""

print("Given an object's mass and velocity, calculate its kinectic energy.", end="\n\n");

input("Press ENTER to start execution ... \n");

# Get mass of the object.
while(True):
    value = input("Enter the mass of the object: ");
    # MASS can't be ZERO or -VE number.
    if (value == "" or float(value) < 0):
        print("Invalid MASS, try again!", end="\n\n");
    else:
        mass = float(value);
        break;

print("\n");

# Get velocity of the object.
while(True):
    value = input("Enter the velocity of the object: ");
    # VELOCITY can't be empty.
    if (value == ""):
        print("Invalid VELOCITY, try again!", end="\n\n");
    else:
        velocity = float(value);
        break;

print("\n");

# KE = (1/2)mv^2 
kinecticEnergy = (1/2) * mass * (velocity ** 2);

print("Given the mass(%.2f) and velocity(%.2f) of an object, its kinectic energy will be %.2f joules." % (mass, velocity, kinecticEnergy), end="\n\n");

input("Press ENTER to exit ... \n");
