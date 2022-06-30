# This program takes a users input of a number of days
# Then outputs the hours, minutes and seconds to screen
#

# This block asks the user for input as a number of days and defines the variables
days = int(input("Please enter an number of days and press enter: "))
hours = days*24
minutes = hours*60
seconds = minutes*60

# This block calculates the days to hours, minutes and seconds and outputs to screen
print("In", days, "days there are ...")
print(hours, "hours")
print(minutes, "minutes")
print(seconds, "seconds")
