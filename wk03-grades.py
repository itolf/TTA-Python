# This program asks for the users exam marks out of 100
# Then grades the user and outputs the result to screen
#

# This block asks for the users exam mark out of 100 then prints the output to screen
score = int(input("Hello, please enter your exam score between 0 and 100... "))

# This block checks the input and grades it accordingly
if score >= 90:
    print("\nCongratulations! Your grade is an A*")
elif score >= 80:
    print("\nWell done! Your grade is an A")
elif score >= 70:
    print("\nNice job! Your grade is a B")
elif score >= 60:
    print("\nNot bad! Your grade is a C")
else:
    print("\nYou will need to score higher to be graded!")
