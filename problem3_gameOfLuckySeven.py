"""
Program : problem3_gameOfLuckySeven.py
Author  : Jigar R. Gosalia
Verion  : 1.0
Course  : CSC-520 (Homework 1)
Prof.   : Srinivasan Mandyam

Game of lucky sevens
--------------------

1. Player enters bet.
2. Player presses enter to roll the dices.
3. If the dots count equal to 7 then player wins $4.
4. If the dots count not equal to 7 then player looses $1.
5. Repeat steps 1 to 4 till the player looses game i.e. amount is $0.
"""

from random import randint;

# Constants
LUCKY_SEVEN = 7;
WIN_AMOUNT = 4;
LOOSE_AMOUNT = 1;
count = 0;
bet = 0;

print("Welcome to Game of Lucky Sevens.", end="\n\n");

print("Roll the dices, if you get 7 then you win else you loose!", end="\n\n");

input("Press ENTER to start execution ... \n");

# Get starting balance from the player.
while (True):
    value = input("Please enter your bet: $");
    if (value == "" or not value.isdigit() or int(value) <= 0):
        print("ERROR : Bet should be a whole number greater than $0 to start", end="\n\n");
    else:
        amount = int(value);
        break;

input("Press ENTER to roll the dices ... ");

# Keep on playing game until either the amount is less than or equal to $0 and player looses.
while(amount != 0):
    # Skip accepting bet for the first time as player has already entered bet amount.
    if (count != 0):
        betValue = input("Please enter your bet: $");
        # Error appropriately if the bet is less than $0 or greater than balance.
        if (betValue == "" or not betValue.isdigit() or int(betValue) <= 0 or int(betValue) > amount):
            print("ERROR : Bet should be a whole number greater than $0 and  less than max balance $%d" % (amount), end="\n\n");
            continue;
        bet = int(betValue);
        input("Press enter to roll the dices ... ");
    amount = amount - bet;
    count += 1;
    # Roll the dices.
    diceOne = randint(1, 6);
    diceTwo = randint(1, 6);
    dotsCount = diceOne + diceTwo;
    # Check whether player WIN or LOOSE
    if (dotsCount == LUCKY_SEVEN) :
        amount = amount + bet + WIN_AMOUNT;
        result = "WIN"
    else:
        amount = amount + bet - LOOSE_AMOUNT;
        result = "LOOSE"
    # Display the results for the roll.
    print("Roll#(%d) DotsCount(%d) Win/Loose(%s) Balance($%d)\n" % (count, dotsCount, result, amount));

print("You Loose, Game Over!", end="\n\n");

input("Press ENTER to exit ... \n");
