#  queue in python

# The Queue is a linear data structure
# Stores items in first in first Out(FIFO) manner

# Queue operations

# 1. Enqueue: Adds an item to the queue
# 2. Dequeue: Removes an item from the queue (first elements)
# 3. Front: Get the front from queue
# 4. Rear: Get the last item from queue

l=[]
while True:
    c=int(input('''
    1 push elements
    2 pop elements
    3 Front elements
    4 Last elements
    5 display elements
    6 exit
                '''))
    if c==1:
        n=input("Enter the value:- ")
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("empty list")
        else:
            del l[0]
            print(l)
    elif c==3:
        if len(l)==0:
            print("empty Queue") 
        else:
            print("first queue value:- ", l[0])
    elif c==4:
        if len(l)==0:
            print("empty list")
        else:
            print("last queue:- ",l[-1])
    elif c==5:
        print("display element",l)
    elif c==6:
        break;

        

