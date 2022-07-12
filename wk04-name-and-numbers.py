# Ian Tolfrey
# 05-07-2022
# This program takes user input of name and two numbers then outputs them to screen

# Defining the variables
name = input("Please enter your name: ")
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a second number: "))

# Checks input number values and outputs to screen
if num1 > num2:
    print("The numbers you chose are: ",num2,num1)
else:
    print("The numbers you chose are: ",num1,num2)
