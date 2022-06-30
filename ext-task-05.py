# This program calculates the radius and depth from user inputs
# Then calculates the volume and outputs to screen
#

# This block imports 'math' libaries
import math

# This block asks user for radius and depth inputs and defines the variables
radius = int(input("Please enter the radius:"))
depth = int(input("Please enter the depth:"))
volume = 0

# This block calculates the volume and outputs to screen
area = math.pi*(radius**2)
volume = area*depth
print("The total volume is", round(volume, 3))
