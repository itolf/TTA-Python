# This program asks user to input a number within the range of 10-20
# Then outputs to screen if wrong values have been entered
#

# This block prompts user to input a number
number = int(input("Please enter a number between 10 & 20: "))

# This block checks the user input against the range for a valid number
if number >= 10 and number <= 20:
    print("Thank you, you chose number", number)
else:
    print("The number", number, "is out of range")
