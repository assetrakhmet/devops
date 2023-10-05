var1="h"
print(type(var1))  #<class 'str'>
var1=True
print(type(var1))  #<class 'bool'>
#All of this fils has a constructor function file.
#Constructor float --> makes the float()
#Constructor int --> makes the int()
#Constructor bool --> makes the bool()

In python we can also convert data types to each other
using constructor function of that specific type.
var1 = 5.9
print(type(var1)) # <class 'float'>
print(var1) # 5.9
var1 = int(var1) #making integer just removes the decimal point
print(type(var1)) # <class 'int'>
print(var1) # 5
var1 = float(var1)
print(type(var1)) # <class 'float'>
print(var1) # 5.0

# incompatible type example 

s = "6"

print (type(s))

s = int(s) 
print (type(s))
