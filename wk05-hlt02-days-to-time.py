'''
Ian Tolfrey
16/07/2022
This program takes a users input of a number of days then outputs the hours, minutes and seconds to screen
'''

print ('\033[40m' + "\n\t<<<<••••  DAYS TO HOURS/MINUTES/SECONDS CONVERTION  ••••>>>>\n" + '\033[0m')

# This block asks the user for input as a number of days and defines the variables
days = int(input("Please enter a number of days and press enter: "))
hours = days*24
minutes = hours*60
seconds = minutes*60

# This block calculates the days to hours, minutes and seconds and outputs to screen
print("In", days, "days there are ...")
print(hours, "hours")
print(minutes, "minutes")
print(seconds, "seconds")


print('\033[40m' + "\n\t<<•• END OF PROGRAM ••>>\n" + '\033[0m')
