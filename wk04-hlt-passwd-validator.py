# Ian Tolfrey
# 10-07-2022
# This program asks user for a password and validates it

import re # importing 'regular expressions library'

def validate(): # subprogram to check and validate the users password against the stated criteria
    while True:
        password=input("Enter a password: ")
        if len(password)<8:
            print("Make sure your password is at lest 8 letters")
        elif re.search('[0-9]',password) is None:
            print("Make sure your password has a number in it")
        elif re.search('[A-Z]',password) is None:
            print("Make sure your password has a capital letter in it")
        else:
            print("Your password has been accepted:")
            break

validate() # calling the subprogram
