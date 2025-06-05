# set 
# set is unordered and unindex, it is work unique time
# functions in set
# add()
# pop()
# set()
# remove()
# clear()
# discard()
# update()

# A set is a collection which is unordered and 
# unindexed, that is iterable, mutable, and has
# no duplicate elements.

# In python sets are written with curly brackets

s={10,20,30,40,50} 
print(s)
print()

for a in  s:
    print(a)
print()
# set is not get index number
# remove()
# if the item to remove does not exist, remove() will raise an error

s={10,20,30,40,50,60}
s.remove(20)
print(s)
print()

# discard()
# if the item to remove does not exist, discard() will NOT raise an error.
s={12,13,14,15,16}
s.discard(13)
print(s)
print()


# set()
l=[10,20,30,40]
s=set(l)
print(s)
print()

# pop()
s={45,55,56,87,12}
print(s.pop())
print(s.pop())
print(s)

# clear()
s={10,20,30,40,50}
s.clear()
print(s)
print()

# add()
s={10,20,30,45}
s.add(89)
print(s)
print()

# update
s={23,24,25,54,32}
l=[10,20,25]
s.update(l)
print(s)



