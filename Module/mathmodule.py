# math module
# Return the ceiling of x, the smallest integer greater than or equal
# to x. If x is not float, delegates to x_ceil_(), which should return an integer
# an integral value.


# if the value is float then it return greater value or it is not float
# then its returns same value 
import math

x=11
print(math.ceil(x))
y=13.1
print(math.ceil(y))


# fabs function return float value
x=10
print(math.fabs(x))

# math.factorial
# return x factorial as an integer. Raises Value 
# error if x is not integral or is negative.

x=5
print(math.factorial(x))

# math.floor 
# it return before points value

y=10.23
print(math.floor(y))

# MATH.FSUM(ITERABLE)
# Return an accurate floating point sum of values in the iterable
l=[10,20,30,40]
print(math.fsum(l))

# math.sqrt()
# Returns the square root of x

s=16
print(math.sqrt(s))