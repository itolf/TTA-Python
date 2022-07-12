# Ian Tolfrey
# 09/07/2022
# This program checks a user to see if they are vaild to drive in the UK

# This block defines the variables
age=int(input("Please enter your age:\n"))
license=input("Do you hold a driving license, y(yes) or n(no)?:\n")

#print (age)+(license) # this tests output

if age>=17 and license=="y":
    print("You are valid to drive in the UK!")
else:
    print("You are not legally able to drive in the UK!")
