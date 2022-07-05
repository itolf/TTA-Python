# This program creates a random number
# Then get the user to inout guesses until right
# The outputs the number of guesses taken 

# This block defines a variable then asks for user input
compnum = 50
guess = int(input("Can you guess the number I am thinking of? "))
count = 1

# This block is the while loop get user input
while guess != compnum:
    if guess < compnum:
        print("Too low!")
    else:
        print("Too high!")
    count = count+1
    guess = int(input("Have another guess: "))
print("Well done, you took", count, "attempts!")
