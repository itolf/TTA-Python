'''
Ian Tolfrey
16/07/2022
This program checks a user to see if they are vaild to        in the UK
'''

print ('\033[40m' + "\n\t<<<<••••  AGE VALIDATION CHECKER  ••••>>>>\n" + '\033[0m')

# This block defines the variable age
age=int(input("Please enter your age: "))

if age>=18:
    print("You are valid to vote in the UK!")
elif age==17:
    print("You are able to learn to drive and vote in the UK!")
elif age==16:
    print("You are allowed to buy a lottery ticket, learn to drive and vote in the UK!")
else:
    print("Sorry, your age restricts you. You can go trick or treating!")

print('\033[40m' + "\n\t<<•• END OF PROGRAM ••>>\n" + '\033[0m')
