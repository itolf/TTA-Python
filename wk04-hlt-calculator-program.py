# Ian Tolfrey
# 12-07-2022
# This program run calulations for the user from a menu

# Subprogram to get user input and call correct Subprogram for the calculation
def calc():
    global userNumber1 # decalring the global variables
    global userNumber2

    print("\n\t====>>>> MENU-CALC <<<<====\n")
    choice=input("What calculation would you like to do? \n\n1> Addition: \n2> Subtraction: \n3> Division: \n4> Multiplication: \n") # displaying calculator options
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

def addition(): # addition subprogram
    sum=userNumber1+userNumber2
    print("The answer is: ",sum)

def subtraction(): # subtraction subprogram
    sum=userNumber1-userNumber2
    print("The answer is: ",sum)

def division(): # division subprogram
    sum=userNumber1/userNumber2
    print("The answer is: ",sum)

def multiplication(): # multiplication subprogram
    sum=userNumber1*userNumber2
    print("The answer is: ",sum)

calc() # calling the subprogram calc to run
