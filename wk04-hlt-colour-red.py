# Ian Tolfrey
# 12/07/2022
# This program checks user input with the or operator

# This block asks for user input and defines the variable
colour = input("What is your favorite colour?")

# This block checks user input and returns output to screen
if colour == "red" or colour == "Red" or colour == "RED":
    print("I like the colour", colour, ("too"))
else:
    print("I don't like the colour", colour, "I prefer Red!")
