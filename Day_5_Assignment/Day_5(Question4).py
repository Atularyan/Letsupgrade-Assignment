""""
Question 4
Implement dequeue operation of the queue
"""
def enqueue(x):
    global f, r
    if r==(size-1):
        print("Overflow")
        return
    if r==-1:
        f=r=0
    else:
        r+=1
    l.insert(r,x)

def dequeue():
    global f, r
    if f==-1:
        print("Underflow")
        return
    a = l.pop(f)
    if f==r:
        f=r=-1
    else:
        r-=1
    print("Poped element = ",a)
def display():
    global f,r
    if f==-1:
        print("Underflow")
        return
    for i in range(f,r+1):
        print(l[i],end=" ")
    print()

l=list()
f=-1
r=-1
size=5
enqueue(10)
enqueue(20)
enqueue(30)
enqueue(40)
enqueue(50)
display()
dequeue()
display()
