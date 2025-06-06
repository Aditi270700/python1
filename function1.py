# how to make normal function
#  user defined function

# A function is a block of statements which can be used repetitively in a program,
# it saves the time of a developer, In python concept of function is same
# as in other languages

# you can pass data, known as parameters, into a function.

#  creating a Function

# In python a function using the def keyword

def simplefunction():
    print("welcome aditi")
simplefunction()
simplefunction()
simplefunction()
print()

# how to pass argument

def sumdata(a,b):
    print(a+b)
n=10
n1=20
sumdata(n,n1)
sumdata(40,50)
print()
# default value set in argument

def adddata(a,b=100):
    print(a+b)
m=50
adddata(m)

# how to return function
# return means we take variable and print variable, or show output

def declarevalue(a,b=5):
    c=a+b
    return c
output=declarevalue(20)
print(output)
print()


def square(x):
    return x*x
s=square(6)
# s=square(7)
print(s)
