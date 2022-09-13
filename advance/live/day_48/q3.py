class Solution:

    def solve(self,A,K):
        n = len(A)
        m = len(A[0])
        x=-1
        y=-1
        i = 0
        j = m-1
        while i < n or j > -1:
            if A[i][j] < K:
                i += 1
            if A[i][j] > K:
                j -= 1
            if A[i][j] == K:
                return i,j
        return -1,-1


solu = Solution()
array = [
    [
        [
            [-10,-5,-2,2,4,7],
            [-7,-4,-1,3,6,9],
            [-2,3,5,7,10,11],
            [-2,3,5,7,11,12],
        ],
        12
    ],
    ]
for A in array:
    ans = solu.solve(A[0],A[1])
    print("output for ",A," is ",ans)

# python3 advance/live/day_48/q3.py