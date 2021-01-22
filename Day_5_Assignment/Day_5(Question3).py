"""
Question 3
Implement pop operation of the stack
"""
def push(x):
    global l, top, size
    if top==(size-1):
        print("Overflow")
        return
    top+=1
    l.insert(top,x)

def pop():
    global l, top, size
    if top==-1:
        print("Underflow")
        return
    a=l.pop(top)
    top-=1
    print("Poped element = ",a)
def display():
    global top,l,size
    if top==-1:
        print("Underflow")
        return
    for i in range(top,-1,-1):
        print(l[i],end=" ")
    print()

l=list()
top=-1
size=5
push(10)
push(20)
push(30)
push(40)
display()
pop()
display()