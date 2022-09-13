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

    def getFouorPointsFromTwo(self,first,fourth):
        second = [first[0],fourth[1]]
        third = [fourth[0],first[1]]
        return [first,second,third,fourth]

    def solve(self,A,Q):
        n = len(A)
        m = len(A[0])
        qN = len(Q)
        pfSum = self.getPrefixSumMatrix(A)
        ans = []
        for i in range(qN):
            query = Q[i]
            x1 = query[0]
            y1 = query[1]
            x2 = query[2]
            y2 = query[3]

            sum = pfSum[x2][y2]
            if y1 > 0:
                sum = sum - pfSum[x2][y1-1]
            if x1 > 0:
                sum = sum - pfSum[x1-1][y2]
            if x1 > 0 and y1 > 0:
                sum = sum + pfSum[x1-1][y1-1]
            ans.append(sum)
        return ans



solu = Solution()
array = [
    [
        [
            [7,2,1,0,3],
            [3,1,2,3,9],
            [6,3,2,4,1],
            [3,1,2,1,4],
            [2,-1,6,2,3],
            [-1,3,2,1,4]
        ],
        [
            [2,1,4,3],
            [3,2,5,4]
        ]
    ],
    [
        [
            [2,-1,3,1],
            [4,2,3,5],
            [-1,2,1,0]
        ],
        [
            []
        ]
    ]
    ]
for A in array:
    ans = solu.solve(A[0],A[1])
    print("output for ",A," is ",ans)
    print("")

# python3 advance/live/day_48/q1.py