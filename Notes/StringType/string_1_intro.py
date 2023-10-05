# Ask user to enter a string 
# print the length of the given string, and print the 
# 5th letter from string.

s = input("Enter anythin:")

# What is the length for this string?
print(len(s))
# Which index number we should find in string?
# i need to find the letter at index 4
print(s[4]) #this will bring the 5th character in string.

# Note! If the index number we are trying to access doesn`t
# exist in string, it will generate InderError.

# Refactor this code so that it wouldn`t generate an error when
# user enters a string that doesn`t have index 4. 

s = input("Enter anything")
print(len(s))

print = input("your password is valid")