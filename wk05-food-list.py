# Ian Tolfrey
# 12/07/2022
# This program prints and item from a python list

import random

food=["Chilli","Chicken Tikka","Chinese","Fish & Chips","Roast Dinner"]
print(food)
print(food[0])
print(len(food))
number=random.randint(0,4)
print(number)
print("\nI chose: ",food[number])
#another way is to use the random.choice(food)
print("or you could have: ",random.choice(food))
