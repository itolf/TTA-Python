# Ian Tolfrey
# 05-07-2022
# This program generates a times table for the user

# This block defines the subprograms
def times2():
    print("\n*** 2 TIMES TABLE ***")
    num1=1

    for num2 in range(2,25,2):
        print(num1," x2 =",num2)
        num1=num1+1

def times3():
    print("\n*** 3 TIMES TABLE ***")
    num1=1

    for num2 in range(3,37,3):
        print(num1," x3 =",num2)
        num1=num1+1

def times4():
    print("\n*** 4 TIMES TABLE ***")
    num1=1

    for num2 in range(4,49,4):
        print(num1," x4 =",num2)
        num1=num1+1

def times5():
    print("\n*** 5 TIMES TABLE ***")
    num1=1

    for num2 in range(5,61,5):
        print(num1," x5 =",num2)
        num1=num1+1

def times6():
    print("\n*** 6 TIMES TABLE ***")
    num1=1

    for num2 in range(6,73,6):
        print(num1," x6 =",num2)
        num1=num1+1

def times7():
    print("\n*** 7 TIMES TABLE ***")
    num1=1

    for num2 in range(7,85,7):
        print(num1," x7 =",num2)
        num1=num1+1

def times8():
    print("\n*** 8 TIMES TABLE ***")
    num1=1

    for num2 in range(8,97,8):
        print(num1," x8 =",num2)
        num1=num1+1

def times9():
    print("\n*** 9 TIMES TABLE ***")
    num1=1

    for num2 in range(9,109,9):
        print(num1," x9 =",num2)
        num1=num1+1

def times10():
    print("\n*** 10 TIMES TABLE ***")
    num1=1

    for num2 in range(10,121,10):
        print(num1," x10 =",num2)
        num1=num1+1

def times11():
    print("\n*** 11 TIMES TABLE ***")
    num1=1

    for num2 in range(11,133,11):
        print(num1," x11 =",num2)
        num1=num1+1

def times12():
    print("\n*** 12 TIMES TABLE ***")
    num1=1

    for num2 in range(12,145,12):
        print(num1," x12 =",num2)
        num1=num1+1

# This block asks user for a selection
table=int(input("Please enter a times table from 2 to 12: "))

# This block takes input and runs the relevant subprogram
if table==2:
    times2()
elif table==3:
    times3()
elif table==4:
    times4()
elif table==5:
    times5()
elif table==6:
    times6()
elif table==7:
    times7()
elif table==8:
    times8()
elif table==9:
    times9()
elif table==10:
    times10()
elif table==11:
    times11()
elif table==12:
    times12()
