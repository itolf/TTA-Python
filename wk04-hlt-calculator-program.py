# Ian Tolfrey
# 12-07-2022
# This program run calulations for the user from a menu

def calc():
    global userNumber1
    global userNumber2

    print("\n\t====>>>> MENU-CALC <<<<====\n")
    choice=input("What calculation would you like to do? \n\n1> Addition: \n2> Subtraction: \n3> Division: \n4> Multiplication: \n")
    userNumber1=int(input("Please enter your first number: "))
    userNumber2=int(input("Please enter your second number: "))
    if choice=="1":
        addition()
    elif choice=="2":
        subtraction()
    elif choice=="3":
        division()
    else:
        multiplication()

def addition():
    sum=userNumber1+userNumber2
    print("The answer is: ",sum)

def subtraction():
    sum=userNumber1-userNumber2
    print("The answer is: ",sum)

def division():
    sum=userNumber1/userNumber2
    print("The answer is: ",sum)

def multiplication():
    sum=userNumber1*userNumber2
    print("The answer is: ",sum)

calc()
