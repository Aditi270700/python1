# How to Build Simple Calculator in Python

print('''
+ Add
- subtract
* Multiply
/ Divide
''')

num1=int(input("Enter any number1:-"))
num2=int(input("Enter any number2:-"))
operator=input("Enter the operator..+,-,/,* :- ")
if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    print(num1/num2)
else:
    print("invalid operator")
    