# list comprehension
l =[]
for a in range(1,101):
    l.append(a)
print(l)

print("")
n = [h for h in range(1,101) if h%2==0]
print(n)

print("")
s="hello"
d=[g for g in s]
print(s)
print(d)