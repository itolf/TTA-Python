'''
Ian Tolfrey
16/07/2022
This program asks for users name and changes the case depening on the name length
'''

print ('\033[40m' + "\n\t<<<<••••  NAME CASE CHANGER  ••••>>>>\n" + '\033[0m')

firstName=input("Please enter your name: ")#

if len(firstName)<5:
    lastName=input("Please enter your surname: ")
    print(firstName.upper(), lastName.upper())
else:
    print(firstName.lower())

print('\033[40m' + "\n\t\t<<•• END OF PROGRAM ••>>\n" + '\033[0m')
