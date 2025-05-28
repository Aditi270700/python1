# function 
# find()
# index()
# isalpha()
# isdigit()
# isalnum()

# find is used to find return index number
w="welcome"
print(w.find('e',2)) # start from 2
print(w.find('e'))
print(w.find('x')) # return -1 because x is not present in string

# index()
w="welcome"
# print(w.index('z')) return error runtime
print(w.index('l'))

# isalpha()
# if all alphabet present in string return true if not present return false
w="welcome"
print(w.isalpha())
s="edffd4656"
print(s.isalpha())


# isdigit()
# it is return true if string is present digit, if digit is not present return false
w="123456"
print(w.isdigit())


# isalnum()
# it is return true alphabet or number present in string or 
# special character present it return false
w="welcome456612"
print(w.isalnum())
s="dfd546565$%%^"
print(s.isalnum())
t="ghjklhjk 123456"
print(t)  # return false beacause space is also count like special character

