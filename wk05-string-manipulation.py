# Ian Tolfrey
# 13/07/2022
# String manipulation and validation

word=input("\nPlease enter a string of words: ") # requesting user entered string

print("\nOrginal word is ... ",word) # prints the string
print("\nUpper case :",word.upper()) # prints string in upper case
print("\nLower case :",word.lower()) # prints string in lower case
print("\nCapitalised :",word.capitalize()) # capitalises the first word
print("\nTitled words :",word.title()) # capitalises each word in the string
print("\nWord count :",word.count("e"),"in this word") # prints how many words in the string
print("\nFind word :",word.find("c")) # prints how many of a letter appear in the string
print("\nLength of word \n",len(word)) # prints total length of the string including spaces
print() # blank line
print(word.isdigit()) # checks the string for numberical characters
print() # blank line
print(word.isalpha()) # checks the string for alpha characters

findme=input("\nwhat letter to you want to find? ") # asks user to input a word to find
if word.find(findme)<0:
  print ("sorry letter not found")
else:
  print("letter is at position : ",word.find(findme))
