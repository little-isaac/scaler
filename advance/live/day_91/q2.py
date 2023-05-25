"""
Maximum element in every window of size 'K'

"""
from collections import deque

class Solution:
    def solve(self, A, K):
        n = len(A)
        a = deque()
        a.append(A[0])
        ans = []
        for i in range(1,K):
            while len(a) > 0 and a[-1] < A[i]:
                a.pop()
            a.append(A[i])
        ans.append(a[0])
        for i in range(K,n):
            addEle = A[i]
            removeEle = A[i-K]
            if a[0] == removeEle:
                a.popleft()
            while len(a) > 0 and a[-1] < addEle:
                a.pop()
            a.append(addEle)
            ans.append(a[0])
        return ans




if __name__ == "__main__":
    solu = Solution()
    array = [
        [[10,1,9,3,7,6,5,11,8], 4]
    ]
    for A in array:
        ans = solu.solve(A[0],A[1])
        print("output for ",A," is ",ans)

