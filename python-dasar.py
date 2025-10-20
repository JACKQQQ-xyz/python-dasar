# cast from str to int
str_numbers = "456"
str_numbers_to_int = int(str_numbers)
print("Before casting :", str_numbers, ", the data type is",
type(str_numbers))
print("After casting :", str_numbers_to_int, ", the data type is",
type(str_numbers_to_int))

# Output
# Before casting : 456 , the data type is <class 'str'>
# After casting : 456 , the data type is <class 'int'>

print("")

# casting from int to str
integer = 12345
integer_to_str = str(integer)
print("Before casting :", integer, ", the data type is", type(integer))
print("After casting :", integer_to_str, ", the data type is",
type(integer_to_str))

# Output
# Before casting : 12345 , the data type is <class 'int'>
# After casting : 12345 , the data type is <class 'str'>

print("")

# casting from int to bool
num_int = 1
num_bool = bool(num_int)
print(num_bool, type(num_bool))
num_int = 0

num_bool = bool(num_int)
print(num_bool, type(num_bool))

# Output
# True <class 'bool'>
# False <class 'bool'>

print("")

# Koding comparison operators
# Equal to
8 == 8
# Not equal to
8 != 9
# Greater than
8 > 9
# Less than
8 < 9
# Less than
8 <= 9
# Less than
9 >= 9

# Koding logical operators
a = True
b = True
print(a and b)
print(a or b)
print(not b)
#logic
5 > 6 and 6 < 7

# Output
# True
# True
# False

print('')

#Koding arithmetic operators
e = 8
f = 2
# Summation
sum = e + f
print(f"The sum of e with f is : {sum}\n")
# Reduction
red = e - f
print(f"The reduction of e with f is : {red}\n")

# Multiplication
multi = e * f
print(f"The multipication of e with f is : {multi}\n")
# Division
divi = e / f
print(f"The quotient of e with f is : {divi}\n")
# Modulo
mod = e % f
print(f"The remainder of e with f is : {mod}\n")
# Power
pow = e ** f
print(f"The power of e of f is : {pow}\n")

# Output
# The sum of e with f is : 10

# The reduction of e with f is : 6

# The multipication of e with f is : 16

# The quotient of e with f is : 4.0

# The remainder of e with f is : 0

# The power of e of f is : 64


