'''
Ian Tolfrey
14/07/2022
This program takes an alphanumerical password and cracks it
'''

print ("\n\t ##### Welcome to the password cracker #####\n")

userPass = input("\n\t Please enter your password: ") # taking input from user

password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', # storing alphanumerical characters to a list called password
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v',
            'w', 'x', 'y', 'z','0','1','2','3','4','5','6','7','8','9']

#***DEPRICATED***pin=['0','1','2','3','4','5','6','7','8','9'] # storing numbers to a list called pin ***numbers added to variable password now for ease of use***

guess = "" # initialises an empty string
passw=[] # initialises an empty list

for i in range(0,len(userPass)): #loops for the length of the password

    while guess != userPass[i]: # using while loop to match letters of the password until one of them matches user_pass
        for y in range(0,len(password)): # length of user password
            guess=password[y] # loops through the letters in password
            #print(password[y]) # output for testing
            if guess==userPass[i]:
                break

    passw.append(guess) # appends the guess to the list passw

print ("\nyour password is ",*passw,sep="") # prints out the passw removing ""
#print ("your password is ",passw)

print("\n\t*** END OF PROGRAM ***")
