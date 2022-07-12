# Ian Tolfrey
# 05-07-2022
# This program generates a random number then asks the user to define the range

import random # this imports the 'random' lbrary for the program

guess=0 # defining the variable outside of the subprogram

# This block asks the user for input
def choose():
    name=(input("Please enter your name: "))
    guess=int(input("Enter a number from 1 to 10! "))

print("\n====>>>>GUESS THE NUMBER<<<<====\n")
number = random.randint(1,10) # this generates the random number and stores the value in the variable 'number'

choose()

# This block uses a loop to continue the guessing until the right answer is chosen
while guess==number:
    print("WOW "+name+"! Well done you are correct!")
    if guess != number:
        print("Sorry "+name+" you have chosen incorrectly!")
