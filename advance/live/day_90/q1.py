"""
Queue implementation using LL


In python

= queue
myQueue = queue.Queue()
myQueue.put(ele)
myQueue.get()
myQueue[0]
myQueue[-1]
"""

class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    front = None
    rear = None
    size = 0
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enque(self, x):
        # insert x at the end of q
        node = Node(x)
        self.size = self.size + 1
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def deque(self):
        # remove first element from q
        if self.size == 0:
            return None
        self.size = self.size - 1
        ele = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return ele.data

    def front(self):
        # first element
        return self.front

    def rear(self):
        # last element
        return self.rear

    def __str__(self) -> str:
        s = ""
        temp = self.front
        while temp is not None:
            s = s + " "+ str(temp.data)
            temp = temp.next
        return s

# solu = Solution()
# array = [
#     [] ,
# ]
# for A in array:
#     ans = solu.solve(A[0],A[1])
#     print("output for ",A," is ",ans)

