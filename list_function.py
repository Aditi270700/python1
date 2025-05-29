# function for delete element from list-

# del()
# pop()
# remove()
# clear()

l = [20,30,40,50]
del l[1]
print(l)
print("")
s = [10,20,30,40,50]
# pop return delete value
print(s.pop(2))
print(s)
print("")
#  we use remove the particular value to delete, pass in the bracket
t = [10,20,50,54,69]
t.remove(54)
print(t)
print("")
# clear remove all list items, we don't put any index and value in the list
u = [10,20,30,40]
u.clear()
print(u)

# update element from list-
print("")
l = [20,30,40,50]
l[0]=89
print(l)

# function for update Element from list

# insert()
# append()
# extends()
print("")
# insert function to insert value not update
l = [20,30,40,50]
l.insert(0,10)
print(l)
print("")

# append()
# append insert all the value like list in last
s = [20,40,60,80,100]
t=[46,21,32]
s.append(t)
print(s)
print("")
# extend()
# extend put the value only from last
v = [20,30,40,50,60]
r = [21,30]
v.extend(r)
print(v)