# Random is a module or function

# random()  Returns a random float between 0 and 1
# shuffle()  takes a sequence and returns the sequence in a random order
# uniform()   Returns a random float number between two given parameters

import random 

# return any random number
n=random.randint(2,8)
print(n)


# returns it is not returns 2 and 4 and returns any value
n1=random.randrange(2,4)
print(n1)

# it returns any element of list
l=[10,20,30,40]
lc=random.choice(l)
print(lc)


# we get any float value
r=random.random()
print(r)

# it is shuffle the list element
l=[10,20,30,40,50]
random.shuffle(l)
print(l)


# it is returns also float but between 0 and 1
u=random.uniform(3,9)
print(u)


