# We create a program that asks user an integer value.
# If this integer value is even double the number and print out the result.
# If the number is odd print (You entered an odd number.)

number = int(input("Please enter an integer value:"))

# We should check if the given number is odd or even.
# Can thrse two conditions be True at the same time ?
# No, because either one of them can be True only.
if number % 2 == 0:
    print (number * 2)
elif number % 2 != 0:
    print ("You entered an odd number.")



