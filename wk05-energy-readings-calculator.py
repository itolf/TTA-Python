'''
Ian Tolfrey
14/07/2022
This program takes gas and electricity readings and calculates usage and the costs
'''

print ('\033[40m' + "\n\t<<<<••••  ENERGY READINGS CALCULATOR  ••••>>>>\n" + '\033[0m')

# Defining variables with constant values
electricityPrice = 31.06 # defining the electricity price per kWh variable
electricityStandingCharge = 47.28 # defining the electricity standing charge per day variable
gasPrice = 7.71 # defining the gas price per kWh variable
gasStandingCharge = 32.03 # defining the gas standing charge per day variable

# Requesting user input meter readings
electricityReading = int(input("\nPlease enter your electricity meter reading: "))
gasReading = int(input("\nPlease enter your gas meter reading: "))

# Defining the previous meter reading variables
previousElectricityReading = 86762 # *** how to store incoming reading? ***
previousGasReading = 21563 # *** how to store incoming reading? ***

# Defining the current usage and cost amounts variables
electricityUsage = electricityReading - previousElectricityReading
gasUsage = gasReading - previousGasReading
print("\nElectricity usage is: " + str(electricityUsage) + "kWh per hour") # *** is changing variable to str() for clean concatenation a problem futher on? ***
print("\nGas usage is: " + str(gasUsage) + "kWh per hour") # *** is changing variable to str() for clean concatenation a problem futher on? ***

# Defining the daily costs variables


print('\033[40m' + "\n\t<<•• END OF PROGRAM ••>>\n" + '\033[0m')
