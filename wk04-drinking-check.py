# Ian Tolfrey
# 09/07/2022
# This program checks a user to see if they are allowed to drink alcohol in the UK

# This block defines the variables
age=int(input("Please enter your age:\n"))
food=(input("Are you eating in the restaurant? y(yes) or n(no):\n"))

#print (age) # this is for testing output

if age>=18:
    print("You are allowed to buy alcohol on these premises.")
elif age ==16 or age==17 and food=="y":
    print("You are allowed to drink alcohol with your meal, but someone over 18 must purchase it!")
else:
    print("You are too young to consume alcohol on these premises!")
