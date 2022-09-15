
class Solution:

    def solve(self, A):
        n = len(A)
        i = 0
        while i < n:
            if A[i] < 1 or A[i] - 1 == i or A[i] > n or A[i] == A[A[i]-1]:
                i += 1
            else:
                A[A[i]-1],A[i] = A[i],A[A[i]-1]
        for i in range(n):
            if i+1 != A[i]:
                return i+1
        return n + 1

solu = Solution()
array = [
    [[3,-2,1,2,7]] , # 4
    [[-9,2,6,4,-8,1,3]] , # 5
    [[1,2,5,6,4,3]] , # 7
    [[1,2,1]] , # 3
    [[-4,8,3,-1]] , # 1
    [[9,-14,6,-7,5,12,2,3,8,1]] , # 4
    [[-1,-2,-3,-4]] , # 1
    [[1,1,1,1]] , # 2
    [[4,1,3,3,2]] , # 2
]
for A in array:
    ans = solu.solveA(A[0])
    print("output for ",A," is ",ans)

# python3 advance/live/day_49/q1.py