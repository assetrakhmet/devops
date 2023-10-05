# John wants lose 10 pounds in one month. 
# There are multiple conditions to lose 10 pounds in a month 
# John needs to walk 10000 steps daily  OR needs to run at least
# 4 miles a day.  and Addition to these , John needs eat less 
# than 1500 calories daily. We should create a program to calculate 
# if John can loose weight or not
# daily steps, and running distance daily calory intake will be given by 
# user. Our goal is  to print True when John can loose weight and print False otherwise.




 print(True or True and True )

run_dist = int(input("Enter how many miles do you run daily:"))
steps = int(input("Enter the amount of steps you take daily;"))

is_active = runningdistance or walkingsteps
is_active = run_dist >= 4 or steps >= 10000

# Calory intake 
daily_intake = int(input("Enter the amount of daily calory intake:"))

is_intake = daily_intake < 1500 

# What should the logical operator be between the is_intake and is_active?

weight_loss = is_intake and is_active
# weight_loss = (run_dist >=)
print(weight_loss)

weight_loss = 