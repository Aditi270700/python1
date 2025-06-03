#   dictionary function
# get() pass key under get() and return value
# key() return key
# values() return value
# items() return key and value
# update()
# dict()
# clear()

d={
'name':'python',
'fees': 8000,
'duration':'2 months'
}
# get()
n=d.get('name')
print(n)
print()
# keys()
for a in d.keys():
    print(a)
print()

# value()
for a in d.values():
    print(a)
print()

# items()

for a in d.items():
    print(a)
print()




# for delete
# del
# pop()
# under both use keys

# del is not function del is a key

del d['fees']
print(d)
print()
# pop
d.pop('duration')
print(d)
print()


# dict
c=dict(name='django',fees=2000)
print(c)
print()

# update()
d.update({'fees':5000})
print(d)
print()
# clear()
d.clear()
print(d)
print()

# Dictionary-update
# for add key and value
w={
'fname':'aditi',
'age':25,
'salary':5500
}
print(w)
w['library']="this is my book"
print(w)



