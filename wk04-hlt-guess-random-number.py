# Ian Tolfrey
# 09-07-2022
# This program generates a random number then asks the user to define the range

import random # this imports the 'random' lbrary for the program

# This block asks the user for input
def choose():
    global name=(input("Please enter your name: "))
    global guess=int(input("Enter a number from 1 to 10! "))
    count =+ 1

print("\n====>>>>GUESS THE NUMBER<<<<====\n")
number = random.randint(1,10) # this generates the random number and stores the value in the variable 'number'
print(number) # this is for testing

count=0

choose()

# This block uses a loop to continue the guessing until the right answer is chosen
while guess!=number and count<5:
    print
