class Solution:

    def getPrefixSumMatrix(self,A):
        n = len(A)
        m = len(A[0])
        pfSum = [[0] * m for _ in range(n)]
        for i in range(n):
            pfSum[i][0] =  A[i][0]
            for j in range(1,m):
                pfSum[i][j] = pfSum[i][j-1] + A[i][j]
        # return pfSum
        for j in range(m):
            pfSum[0][j] =  pfSum[0][j]
            for i in range(1,n):
                pfSum[i][j] = pfSum[i-1][j] + pfSum[i][j]
        return pfSum

    def totalSubMatrixCount(self,A):
        n = len(A)
        m = len(A[0])
        t = (n+1)*n * (m+1) * m
        t = t / 4
        return t

    def getElementContribution(self,i,j,n,m):
        return (i+1)*(j+1)*(n-i)*(m-j)

    def solve(self,A):
        n = len(A)
        m = len(A[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                ans += self.getElementContribution(i,j,n,m) * A[i][j]
        return ans

solu = Solution()
array = [
    [
        [
            [],
            [],
            []
        ]
    ],
    [
        [
            [],
            [],
            []
        ]
    ]
    ]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)

# python3 advance/live/day_48/q2.py