# Ian Tolfrey
# 09-07-2022
# This program generates a random number then asks the user to define the range

import random # this imports the 'random' lbrary for the program

print("\n\t====>>>>GUESS THE NUMBER<<<<====\n")
number=random.randint(1,10) # this generates the random number and stores the value in the variable 'number'
#print(number) # this is for testing
name=(input("\nPlease enter your name: "))
print("\nOk "+name+" you have 3 attempts to guess the number between 1 & 10!\n")
count=1

while count<=3:
    guess=int(input("Take a guess:"))
    count+=1
    if guess==number:
        print("Well done "+name+", you guessed the number!\n")
        break
    elif guess<number:
        print("Your guess is too low, please try again.\n")
    else:
        print("Your guess is too high, please try again.\n")

print("\nThanks for playing!")
print("\n\t*** End of program ***")
