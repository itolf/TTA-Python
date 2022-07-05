# This program asks a user for a password twice and compares the input for errors
#
#

# This block takes user inputs
pswd1 = input("Enter a password: ")
pswd2 = input("Enter it again: ")

# This block compares the user inputs and outputs a response
if pswd1 == pswd2:
    print("Thank you")
elif pswd1.lower() == pswd2.lower():
    print("They must be the same case!")
else:
    print("The passwords do not match!")
    
