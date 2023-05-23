"""
Reverse first k elements in queue using 1 stack

"""
from advance.live.day_90.q3 import Solution as Queue
from collections import deque

class Solution:

    def generateArray(self, queue):
        a = []
        while queue.rear is not None:
            a.append(queue.deque())
        return a

    def generateQueue(self, A):
        queue = Queue()
        n = len(A)
        for i in range(n):
            queue.enque(A[i])
        return queue

    def createStack(self,queue,K):
        stack = deque([])
        for i in range(K):
            stack.append(queue.deque())
        return stack

    def solve(self, A, K):
        queue = self.generateQueue(A)
        n = queue.size
        stack = self.createStack(queue,K)
        for i in range(K):
            queue.enque(stack.pop())
        for i in range(n - K):
            queue.enque(queue.deque())
        return self.generateArray(queue)
# solu = Solution()
# array = [
#     [] , 
# ]
# for A in array:
#     ans = solu.solve(A[0],A[1])
#     print("output for ",A," is ",ans)

