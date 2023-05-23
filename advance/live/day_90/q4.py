"""
Generate kth number in series using 1 & 2

"""
from advance.live.day_90.q1 import Solution as Queue

class Solution:

    def solve(self, K):
        if K in [1,2]:
            return K
        queue = Queue()
        queue.enque('1')
        queue.enque('2')
        for i in range(K-1):
            ele = queue.deque()
            queue.enque(ele+'1')
            queue.enque(ele+'2')
        return int(queue.deque())

# solu = Solution()
# array = [
#     [] , 
# ]
# for A in array:
#     ans = solu.solve(A[0],A[1])
#     print("output for ",A," is ",ans)

