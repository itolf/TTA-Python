# Ian Tolfrey
# 12/07/2022
# This program prints and item from a python list

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
