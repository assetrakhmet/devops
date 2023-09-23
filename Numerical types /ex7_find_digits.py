four_digit_number = 1234

# 32 % 10 -> 2
# 49 % 10 -> 9 
# 101 % 10 -> 1

# Note! Every time finding a remainder with 10 gives us 
# last digit from the number.

# 32 // 10 ->



last_digit = four_digit_number%10
three_digit_version = four_digit_number //10

# 9 % 10 -> 9
# 8 % 10 -> 8
# 7 % 10 -> 7
# 6 % 10 -> 6

# 9876 // 10 -> 987.6
# 987.6 // 10 -> 98.76
# 98.76 // 10 -> 9.876
# 9.876 // 10 -> 0.9876


four_digit_num = 9876

last_digit = four_digit_num % 10
print(last_digit)
# I want to remove the last digit
three_digit_version = four_digit_num //10

third_digit = three_digit_version % 10 
print(third_digit)
two_digit_version = three_digit_version // 10

second_digit = two_digit_version % 10
print(second_digit)

first_digit = two_digit_version // 10
print(first_digit)