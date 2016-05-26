"""
Program : problem6_payroll.py
Author  : Jigar R. Gosalia
Verion  : 1.0
Course  : CSC-520 (Homework 1)
Prof.   : Srinivasan Mandyam

A simple text file contains pay roll info as follows <last name> <hourly wage> <hours worked>.

Write a program that takes the input file name from the user, reads the file, calculates the pay and prints a report.

Assume the problem6-data.txt file is available in .txt format.

"""

import os;

# Length of horizontal line.
LENGTH = 60;

print("Read employee details file and calculate each employee's pay and print EMPLOYEE PAYROLL REPORT.", end="\n\n");

input("Press ENTER to start execution ... \n");

# Accept fileName from User.
fileName = input("Enter path to employee data file: ");

# Will be used to pause auto-scrolling.
noOfRecords = 0;

# Keep looping until correct file is read and employee payroll report is not displayed.
while (True):
    # Check if given fileName exists!
    if (os.path.exists(fileName)):
        file = open(fileName, 'r');
        print("\n" * 3);
        print("-" * LENGTH);
        # Employee Payroll Report Header.
        print("EMPLOYEE PAYROLL REPORT".center(LENGTH))
        print("-" * LENGTH);
        # Employee Payroll Report column names.
        print("%-10s %15s %15s %15s" % ("LAST-NAME", "HOURLY WAGES", "HOURS WORKED", "PAY"));
        print("-" * LENGTH);
        # Read each employee details and calculate employee's pay from hourly wages and hours worked.
        for employee in file:
            noOfRecords += 1;
            empDetails = employee.split();
            lastName = empDetails[0];
            hourlyWages = "%6.2f" % (float(empDetails[1]));
            hours = int(empDetails[2]);
            pay = "%10.2f" % (float(empDetails[1]) * hours);
            print("%-10s %15s %15d %15s" % (lastName, "$" + hourlyWages.strip(), hours, "$" + pay.strip()));
            # Pause auto-scrolling after every 15 employee records and wait for user to press ENTER to continue.
            # This is done for better user readability.
            if ((noOfRecords % 15) == 0):
                input("\n\n" + "Press ENTER to continue .... ".center(LENGTH) + "\n\n");
                print("-" * LENGTH);
                print("%-10s %15s %15s %15s" % ("LAST-NAME", "HOURLY WAGES", "HOURS WORKED", "PAY"));
                print("-" * LENGTH);
        print("-" * LENGTH);
        print("\n" * 3);
        break;
    else:
        print("<%s> file doesn't exists, try again!" % (fileName), end="\n\n");
        # Accept fileName from User, as given fileName doesn't exists!
        fileName = input("Enter path to input file: ");

input("Press ENTER to exit ... \n");

