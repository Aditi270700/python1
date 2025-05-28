# python string format() method
# if we use any string,integer between in string, that time we use string .format

# example
txt1 = "welcome to {fname} {lname}".format(fname="aditi",lname="saudagar")
# numbered indexes:

txt2 = "welcome to {0} {1}".format("aditi","saudagar")
# empty placeholders:

txt3 = "welcome to {} {}".format("aditi","saudagar")
print(txt1)
print(txt2)
print(txt3)

text = "my name is {} and my age is {}".format("aditi",25)
print(text)
text1="my name is {fname} and my last name is {lname}".format(fname="Aditi",lname="Saudagar")
print(text1)
text2 = "my age is {1} and my name is {0}".format("aditi",25)
print(text2)

w="welcome {b:>10} to {a:^10} wscubetech".format(a=30,b=40)
print(w)
# {b:10} means it takes 1 character space in output





