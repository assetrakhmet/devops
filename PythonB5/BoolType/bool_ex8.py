#  Leap Year
# A year is leap if it is divisible by 4 but not by 100 
# unless it is also divisible by 400. 
# Write a program that takes a year as input 
# and prints True if it's a leap year, False otherwise.
# 2000, 2024, 2020, 1916, 400....
number = int(input("Enter the year"))
is_divisible_4_but_not_100 = number % 4 == 0 and number % 100 != 0
is_divisible_400 = number % 400 == 0
# print = number % 4 == 0 and number % 400 == 0
# print = (result)
print ( is_divisible_4_but_not_100 or is_divisible_400)

#Note if the number x is divisible by number z it means 
# x % z == 0 evaluates to True. 
# if x % z == 0 is True it means x is divisible by z. 

