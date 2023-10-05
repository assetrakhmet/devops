
# Problem 1: Even or Odd
# We will write a program that prints true when variable `number` is 
# even, and prints False when the number us odd.
# Odd number: 1,3,5,7,9,11,13 etc.
# Even numbeer: 2,4,6,8,10,12 etc.
number = 11

# Even numbers are perfectly divisible by 2, and odd numbers not. 

is_even = number % 2 == 0

print(is_even)