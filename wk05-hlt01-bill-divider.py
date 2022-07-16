'''
Ian Tolfrey
16/07/2022
This program divides up a total bill between a number of people then shares equally
'''

print ('\033[40m' + "\n\t<<<<••••  BILL DIVIDER  ••••>>>>\n" + '\033[0m')

# This block gets the user input and stores it in variables
bill = float(input("Please enter the total amount of the bill £"))
people = int(input("Now enter the amount of people "))
equals = 0

# This block divides the user input amount by the user input of people
equals = bill/people
print("\nEach person pays an equal amount of £", equals)

print('\033[40m' + "\n\t<<•• END OF PROGRAM ••>>\n" + '\033[0m')
