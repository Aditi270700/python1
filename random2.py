# Number guessing game
# python (using Random Module)

import random

Cnumber = random.randrange(1,101)
userInput=int(input("enter your number:-- "))
if userInput>Cnumber:
    print("Computer number",Cnumber)
    print("your guess number is high")
elif userInput<Cnumber:
    print("Computer number",Cnumber)
    print("your guess number is too low")
else:
    print("Computer number",Cnumber)
    print("your guess number is equal")