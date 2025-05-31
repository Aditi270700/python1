# iterate over 2 + list at the same (zip function)
l = [10,20,30,40,50]
l1 = [3,4,5,6,8]
t=len(l)
# s=len(l1)

for a,b in zip(l,l1):
    print(a,b)

for h in range(t):
    print(l[h],l1[h])

# for p in range(s):
#     print(l1[p])