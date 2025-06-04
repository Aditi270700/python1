# tuple 
# tuple is immutable datatype
# tuple is constant it is not changeble 
# tuple is an ordered datatype it is defined in parenthisis()
# single element is not called tuple and comma seperated

# function used in tuple
# min()
# max()
# count()
# sum()
# index()

t=(10,20,30,40,50)
print(type(t))
n=t[4]
print(n)
print()


# l=len(t)
# for a in range(l):
#     print(t[a])
# iteration through a Tuple
# Using a for loop we can iterate though each item in a tuple

for a in t:
    print(a)
print()

# min() function
m=(20,25,30,58,74,12)
k=min(m)
print(k)
print()

# max() function
m=(20,25,30,58,74,12)
k=max(m)
print(k)
print()

# count() function
m=(10,20,30,10,20,10,10)
k=m.count(10)
print(k)
print()

# index()
m=(10,20,30,10,20,10,10)
k=m.index(10)
print(k)
print()
# that value get first it return first getting value

# sum()
m=(10,20,30,10,20,10,10)
k=sum(m,100)  # 100 give default value
print(k)