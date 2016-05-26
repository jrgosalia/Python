"""

Program : problem4_myRange.py
Author  : Jigar R. Gosalia
Verion  : 1.0
Course  : CSC-520 (Homework 2)
Prof.   : Srinivasan Mandyam

Define and test a function myRange.
This function should behave like Python’s standard range function,
with the required and optional arguments.

Do not use the range function in your implementation!

"""

def myRange(first, second=None, third=1):
    """ myRange functions depicts range function in Python. It returns list of numbers given upper limit OR
        lower and upper limit OR lower limit, upper limit and step value

        first  = Acts as Lower and Upper Limit depending on the no. of parameters passed to the function
        second = Upper Limit for the myRange function (default = None)
        third  = Step value for the myRange function (default = 1). """
    myList = []

    # both the limits not present
    if first == None and second == None:
        return myList

    # not possible scenario as if there is one argument
    # it will be treated as "first" as "second" has a default value
    if first == None and second != None:
        return myList

    # Only Upper Limit present
    if first != None and second == None:
        if third != None:
            second = first
            first = 0
            while first < second:
                myList.append(first)
                first += third

    # Both the limits are present
    if first != None and second != None:
        # raise ValueError just like range function when step is ZERO
        if (third == 0):
            raise ValueError("range() arg 3 must not be zero")
        # +ve step or default step=1
        if third > 0:
            while first < second:
                myList.append(first)
                first += third
        # -ve step
        else:
            while first > second:
                myList.append(first)
                first += third


    return myList

def main():
    """ Main method. """
    print("\n" * 10)
    print("Demonstrate range function by writing myRange", end="\n\n");
    input("Press ENTER to start execution ... \n");

    # no parameters (error scenario)
    try:
        print(myRange())
    except Exception as exception:
        print("myRange fails when there are no input parameters and its throws error : " + repr(exception))
    # Upper Limit only
    print(myRange(10))
    # Lower and Upper Limit only
    print(myRange(1, 10))
    # Lower limit, Upper limit and +ve Step value
    print(myRange(1, 10, 2))
    # Lower limit, Upper limit and -ve Step value
    print(myRange(10, -10 , -2))

    # step=0 (error scenario)
    try:
        print(myRange(1, 10, 0))
    except ValueError as error:
        print("myRange fails when step=0 to avoid infinite loop : " + repr(error))
    print("\n")

"""
    Starting point
"""
main()
