# string iteration in python

w='welcome to aditi'
t=len(w)
print(t)
for a in range(t-1,-1,-1):
    print(w[a])


# if we do not use range
s='welcome tthe home'
s=s[-1::-1]
for a in s:
    print(a)