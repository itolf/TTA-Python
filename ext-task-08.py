# This program creates random numbers and gets a user to enter guesses
#
#

# This block imports the 'random' libraries
import random

# This block defines the score variable
score = 0

# This block creates the random numbers and asks user for input and checks the score with output
for i in range(1,6):
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    correct = num1 + num2
    print(num1, "+", num2,"= ")
    answer = int(input("Your answer: "))
    print()
    if answer == correct:
        score = score + 1
    print("You scored",score, "out of 5")
