"""
queue implementation using stack

"""
from collections import deque

class Solution:
    front = None
    rear = None
    size = 0
    mainStack = deque([])
    secondStack = deque([])
    def enque(self, x):
        if self.front is None:
            self.front = x
        self.mainStack.append(x)
        self.size = self.size + 1
        self.rear = x
    def deque(self):
        if len(self.secondStack) == 0 and len(self.mainStack) == 0:
            return None
        if len(self.secondStack) == 0:
            while len(self.mainStack) > 0:
                self.secondStack.append(self.mainStack.pop())
        self.size = self.size - 1
        ele = self.secondStack.pop()
        if len(self.secondStack) == 0:
            if len(self.mainStack) == 0:
                self.front = None
                self.rear = None
            else:
                self.front = self.mainStack[0]
                self.rear = self.mainStack[-1]
        else:
            if len(self.mainStack) == 0:
                self.front = self.secondStack[-1]
                self.rear = self.secondStack[0]
            else:
                self.front = self.secondStack[0]
                self.rear = self.mainStack[-1]
        return ele
    def deque1(self):
        if self.size == 0:
            return None
        self.size = self.size - 1
        tempStack = deque([])
        while len(self.mainStack) > 0:
            tempStack.append(self.mainStack.pop())
        removedEle = tempStack.pop()
        while len(tempStack) > 0:
            self.mainStack.append(tempStack.pop())
        if len(self.mainStack) == 0:
            self.front = None
            self.rear = None
        else:
            self.front = self.mainStack[0]
            self.rear = self.mainStack[-1]
        return removedEle

    def front(self):
        return self.front
    def rear(self):
        return self.rear

    def __str__(self) -> str:
        s = ""
        temp = self.front
        for i in range(len(self.mainStack)):
            s = s + " "+ str(self.mainStack[i])
        return s


# solu = Solution()
# array = [
#     [] , 
# ]
# for A in array:
#     ans = solu.solve(A[0],A[1])
#     print("output for ",A," is ",ans)

