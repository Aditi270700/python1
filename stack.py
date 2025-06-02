# stack is a linear data structure
# linear data structure means arrange data in a sequence order

# stores items in a last-in/first-out(lifo) or first-In/Last-out(FILO) manner

# stack Operations

# 1. push => Inserting an elements
# 2. pop => Deletion an elements (last element)
# 3. peek => display the last element
# 4. display => display list

l=[]
while True:
    c=int(input('''
         1 push elements
         2 pop elements
         3 peek elements
         4 Display stack
         5 Exit
           ''' ))
    if c==1:
        n=input("Enter the value");
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("empty list")
        else:
            e=l.pop()
            print(e)
            print(l)
    elif c==3:
        if len(l)==0:
            print("empty list")
        else:
            print("Last Stack Value",l[-1])
    elif c==4:
        print("display stack",l)
    elif c==5:
        break;
    
    