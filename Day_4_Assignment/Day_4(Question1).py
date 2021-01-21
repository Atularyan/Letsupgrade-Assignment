"""
Question 1
Implement deletion operation from the end of the linked list and Insertion operation from the
beginning of the linked list
"""



class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def length(head):
    count=0
    while head is not None:
        count=count+1
        head=head.next
    return count
def InsertBeg():
    inputList=[int(ele) for ele in input("Enter values : ").split()]
    head=None
    for currData in inputList:
        if currData==-1:
            break
        newNode=node(currData)
        if head is None:
            head=newNode
        else:
            newNode.next=head
            head=newNode
    return head
def deleteEnd(head,i):
    if i<0 or i>length(head):
        return head
    count=0
    prev=None
    curr=head
    while count<i:
        prev=curr
        curr=curr.next
        if curr==None:
            return head
        count=count+1
    if prev is not None:
        prev.next=curr.next
    else:
        head=curr.next
    return head

def printLL(head):
    while head is not None:
        print(str(head.data)+"->",end="")
        head=head.next
    print("None")
    return
head=InsertBeg()
printLL(head)
i=length(head)-1
k=deleteEnd(head,i)
printLL(k)