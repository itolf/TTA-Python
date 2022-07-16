'''
Ian Tolfrey
12/07/2022
This program is a randomised password cracker
'''

print ('\033[40m' + "\n\t<<<<••••  RANDOMISATION PASSWORD CRACKER  ••••>>>>\n" + '\033[0m')

import random

print ("\n\t ##### Welcome to the password cracker ####\n")

user_pass = input("\n\t Please enter your password : ") # taking input from user

# storing letters of the alphabet to
#password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k',
#            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v',
#            'w', 'x', 'y', 'z','0','1','2','3','4','5','6','7','8','9']

password=['0','1','2','3','4','5','6','7','8','9'] # numbers for pin instead of passwords

guess = "" # initializing an empty string
# using while loop to generate many passwords until one of
# them matches user_pass
while (guess != user_pass):
    guess = ""
    # generating random passwords using for loop
    for letter in range(len(user_pass)): # generates the number of characters
        #guess_letter = password[random.randint(0, 25)]
        guess_letter = password[random.randint(0,9)]
        guess = str(guess_letter) + str(guess) # creates a guess
    # printing guessed passwords
    print(guess)

# printing the matched password
print("\n Your password is ",guess)

print('\033[40m' + "\n\t<<•• END OF PROGRAM ••>>\n" + '\033[0m')
