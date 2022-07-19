'''
Ian Tolfrey
18/07/2022
Asks user for names to invite then displays names unless more than 10 are chosen
'''

print ('\033[40m' + "\n\t<<<<••••  PARTY INVITES  ••••>>>>\n" + '\033[0m')

invites = int(input("Please enter the number of friends you wish to invite to the party: "))
list = []

if invites < 10:
    for i in range(0, invites):
        list.append (input("Please enter a name to invite: "))
        print(list[i], "has been invited.")
else:
    print("That is too many people.")

print('\033[40m' + "\n\t\t<<•• END OF PROGRAM ••>>\n" + '\033[0m')
