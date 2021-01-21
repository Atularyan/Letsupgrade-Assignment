"""
Question 3
Write a Python program to find the middle of a linked list.
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def takingInput():
    inputList=[int(ele) for ele in input("Enter Linkedlist values: ").split()]
    head=None
    tail=None
    for currData in inputList:
        if currData==-1:
            break
        newNode=Node(currData)
        if head is None:
            head=newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode
    return head
def printLL(head):
    while head is not None:
        print(str(head.data)+"->",end="")
        head=head.next
    print("None")
    return
def midpoint(head):
    slow=head
    fast=head
    while(fast.next!=None and fast.next.next!=None):
        slow=slow.next
        fast=fast.next.next
    return slow
head=takingInput()
printLL(head)
k=midpoint(head)
print("midpoint = ",k.data)