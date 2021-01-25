"""
Question 2
Implement push, pop and find the minimum element in a stack in O(1) time complexity.
"""

class stack:
    def __init__(self):
        self.data=[]
        self.min=None

    def push(self,x):
        if not self.data:
            self.data.append(x)
            self.min=x
        elif x > self.min:
            self.data.append(x)
        else:
            self.data.append(2 * x - self.min)
            self.min=x

    def pop(self):
        if not self.data:
            print("Stack Underflow")

        top = self.data[-1]
        if top < self.min:
            self.min= 2 * self.min -top
        self.data.pop()

    def minimum(self):
        return self.min

s=stack()
s.push(11)
s.push(7)
s.push(8)
s.push(6)
s.pop()
print("Minimum element : ",s.minimum())
