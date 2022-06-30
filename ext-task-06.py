# This program asks for user input in a number of invitations within the parameters of 1-9
# Then user inputs the names and the program outputs thee names that have been invited
#

# This block asks user input of a number from 1 to 9
invites = int(input("Please enter the number of friends you wish to invite to the party: "))
if invites < 10:
    for i in range(0, invites):
        name = input("Enter a name: ")
        print(name, "has been invited.")
else:
    print("That is too many people.")
