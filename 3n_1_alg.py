"""
Consider the following algorithm to generate a sequence of numbers. 
Start with an integer n. 
If n is even, divide by 2. 
If n is odd, multiply by 3 and add 1. 
Repeat this process with the new value of n, terminating when n = 1. 
For example, the following sequence of numbers will be generated for n = 22: 
22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
"""

def get_choice():
    choicestring = input("Please give me integer between 1 & 1 million: ")
    choice = int(choicestring)
    if choice <1 or choice >1000000:
        print "Please try again, your number is out of range."
        get_choice()
    else:
        return algor(choice)

def algor(choice):
    number = choice
    numblist = [choice]
    while number >1:
        if number % 2 == 0 and number != 1:
            number = number /2
            numblist.append(number)
            print numblist
        elif number % 2 != 0 and number !=1:
            number = number *3 + 1
            numblist.append(number)
            print numblist
        else:
            numblist.append(1)
            print numblist


get_choice()
