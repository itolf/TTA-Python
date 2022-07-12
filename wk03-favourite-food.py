# This program prompts the user to input their favourite foods
# Then concatenates the input and displays to the screen as output
#


# This block asks the user for specific input
print("Hello there, I have a few questions about some of your favourite foods...")
print("Please press enter after each answer.\n")

# Defining the variables with each user input
starter = input("Please tell me what is your favourite starter? ")
print("Thank you.\n")

mainCourse = input("Please tell me what your favourite main course? ")
print("Thank you.\n")

desert = input("Now please tell me what your favourite desert is? ")
print("Thank you.\n")

drink = input("And finally, what is your favourite beverage? ")
print("Thank you.\n")

# This block now outputs the users input to screen
print(("Your favourite meal would consist of all these favourites,"), starter, ("then your favourite meal"),
      mainCourse, ("followed up with your favourite desert"), desert, ("and washed down with none other than"), drink)
