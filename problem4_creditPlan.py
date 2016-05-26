"""
Program : problem4_creditPlan.py
Author  : Jigar R. Gosalia
Verion  : 1.0
Course  : CSC-520 (Homework 1)
Prof.   : Srinivasan Mandyam

The credit plan in a computer store specifies 20% down payment and 12 % annual interest.
Monthly payments are 5% of the listed price minus down payment.

Write a program that takes purchase price as input and display the life time payment in tabular form.

The table headers are Month # starts from 1, Current total balance owed, interest owed for that month,
amount of principle owed for that month, the payment for that month, the balance remaining after payment.

------------
Assumptions:
------------
1. Monthly payments includes monthly installment and monthly interest.
2. Sooner or later, the starting balance will be less than monthly installment, hence at that time monthyly
   installment will be set to ZERO and payer will pay only balance and monthly interest on that balance.

"""

# Constants
DOWN_PAYMENT_PERCENT = 0.20;
ANNUAL_INTEREST_RATE = 0.12;
MONTHLY_PAYMENT_PERCENT = 0.05;
LENGTH = 80;

print("Display lifetime payment plan for given listed price for a computer.", end="\n\n");

input("Press ENTER to start execution ... \n");

# Get the listed price of the computer.
while (True):
    price = input("Enter the listed price of the computer: $");
    if (price == "" or float(price) <= 0):
        print("Invalid listed price, try again!", end="\n\n");
    else:
        listedPrice = float(price);
        break;

# Downpayment is 20% of the listed price.
downpayment = listedPrice * DOWN_PAYMENT_PERCENT;

print("\n");

print("Listed Price: $%.2f" % (listedPrice));

print("Downpayment : $%.2f" % (downpayment));

print("\n\n");

print("-" * LENGTH);

print("LIFETIME PAYMENT PLAN".center(LENGTH), end='\n');

print("-" * LENGTH);

print("%4s | %12s | %10s | %12s | %12s | %12s" % ("Mnth", "Starting Bal", "Mthly Int", "Mthly Inst", "Mthly Paymt", "Remaining Bal"));

print("-" * LENGTH);

# Starting Balance will be listed price minus down payment.
startBalance = listedPrice - downpayment;

# Monthly payments are 5% of principle amount (listed prices minus down payment).
monthlyInstallment = round(startBalance * MONTHLY_PAYMENT_PERCENT, 2);

# Number of Months
month = 0;

# Starting Balance should be greater than ZERO and it should be greater then monthly installment
while (startBalance > 0 and startBalance > monthlyInstallment):
    if (month % 10 == 0 and month != 0):
        input("\n\n" + "Press ENTER to continue ... ".center(LENGTH) + "\n\n");
        print("-" * LENGTH);
        print("%4s | %12s | %10s | %12s | %12s | %12s" % ("Mnth", "Starting Bal", "Mthly Int", "Mthly Inst", "Mthly Paymt", "Remaining Bal"));
        print("-" * LENGTH);
    month += 1;
    # Monthly interest would be Annual Interest / 12 months.
    monthlyInterest = round(startBalance * (ANNUAL_INTEREST_RATE / 12), 2);
    # Monthly payments will be difference of monthly installment and monthly interest.
    monthlyPayment = monthlyInstallment - monthlyInterest;
    endBalance = round(startBalance - monthlyPayment, 2);
    print("%4d | %12.2f | %10.2f | %12.2f | %12.2f | %12.2f" % (month, startBalance, monthlyInterest, monthlyInstallment, monthlyPayment, endBalance));
    startBalance = endBalance;

# Special handling when starting balance is greater than ZERO but less than monthly installment.
# In this case, payer will only pay remaining balance and monthly interest but only monthly installment.
if (startBalance > 0 and startBalance <= monthlyInstallment):
    monthlyInterest = round(startBalance * (ANNUAL_INTEREST_RATE / 12), 2);
    monthlyInstallment = 0;
    monthlyPayment = startBalance + monthlyInterest;
    endBalance = round((startBalance + monthlyInterest) - monthlyPayment , 2);
    print("%4d | %12.2f | %10.2f | %12.2f | %12.2f | %12.2f" % (month + 1, startBalance, monthlyInterest, monthlyInstallment, monthlyPayment, endBalance));

print("-" * LENGTH);

print("\n\n");

input("Press ENTER to exit ... \n");

