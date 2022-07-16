'''
Ian Tolfrey
12/07/2022
This program prints and item from a python list
'''

print ('\033[40m' + "\n\t<<<<••••  DESTINATION LIST  ••••>>>>\n" + '\033[0m')

import random

city=["London","Manchester","Liverpool","Birmingham","Edinburgh"]
print(city)
print(city[0])
print(len(city))
number=random.randint(0,4)
print(number)
print("\nI chose: ",city[number])
#another way is to use the random.choice(city)
print("or you could have visited: ",random.choice(city))

print('\033[40m' + "\n\t<<•• END OF PROGRAM ••>>\n" + '\033[0m')
