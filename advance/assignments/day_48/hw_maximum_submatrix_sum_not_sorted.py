class Solution:
    # @param A : list of list of integers
     # @return an long
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

    def getSumOfSubMatrix(self,pfSum,tl,br):
            x1 = tl[0] -1
            y1 = tl[1] -1
            x2 = br[0] -1
            y2 = br[1] -1
            sum = pfSum[x2][y2]
            if y1 > 0:
                sum = sum - pfSum[x2][y1-1]
            if x1 > 0:
                sum = sum - pfSum[x1-1][y2]
            if x1 > 0 and y1 > 0:
                sum = sum + pfSum[x1-1][y1-1]
            return sum
    def solve(self, A):
        n = len(A)
        m = len(A[0])
        i = 0
        j = m-1
        pfSum = self.getPrefixSumMatrix(A)
        ans = float("-inf")
        for i in range(n):
            for j in range(m):
                sum1 = self.getSumOfSubMatrix(pfSum,[i+1,j+1],[i+1,m])
                sum2 = self.getSumOfSubMatrix(pfSum,[i+1,j+1],[n,j+1])
                sum3 = self.getSumOfSubMatrix(pfSum,[i+1,j+1],[n,m])
                ans = max(ans,sum1,sum2,sum3)
        return ans


solu = Solution()
array = [
    [
        [ 
          [-17,-2],
          [20, 10]
        ],

    ], #
    [
        [
            [-6, -6],
            [-29, -8],
            [3, -8],
            [-15, 2],
            [25, 25],
            [20, -5]
        ]
    ],
    [
        [
            [-6, -21, 27, 19, 19],
            [0, 0, 5, -21, 19],
            [18, -27, -2, -7, 13],
            [-21, -17, -25, -1, 3],
            [0, -9, -6, -16, -5],
            [29, 9, -25, -7, -25]
        ]
    ]
    ]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)