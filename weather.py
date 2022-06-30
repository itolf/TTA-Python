# This progem takes user input and displays varing output depending on the users input
#
#

# User inputs the weather
weather = input("What is the weather like where you are? ")

# this blocks checks user input and prints out varied responces to the users input
if weather == "rain":
    print("You might want to take an umbrella!")
elif weather == "sleet":
    print("Stay home in the warm and dry!")
elif weather == "sun":
    print("Don't forget the sun cream!")
else:
    print("Wear a warm coat!")

# User inputs the temperature, the input string is converted to an integer
temp = int(input("What is the temperature? "))

# this blocks checks user input and prints out varied responces to the users input
if temp >= 30:
    print("WOW! That is very hot")
elif temp <= 10:
    print("It is getting very cold")
else:
    print("It is fairly mild")
