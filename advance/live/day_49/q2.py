class Solution:

    def isOverLapping(self,a,b):
        si = a[0]
        ei = a[1]
        s = b[0]
        e = b[1]
        if s > ei or si > e:
            return False
        return True
    def solve(self, A,B):
        n = len(A)
        ans = []
        isNewAdded = False
        for i in range(n):
            if self.isOverLapping(A[i],B):
                B = [min(A[i][0],B[0]),max(A[i][1],B[1])]
            else:
                if A[i][0] > B[1] and isNewAdded is False:
                    ans.append(B)
                    isNewAdded = True
                ans.append(A[i])
        if isNewAdded is False:
            ans.append(B)
        return ans
solu = Solution()
array = [
    [
        [
            [1,3],[4,7],[10,14],[16,19],[21,24],[27,30],[32,35],[38,41],[43,50]
        ],
        [12,22]
        ] , 
        [
            [
                [1,5],[8,10],[11,14],[15,20],[21,24]
            ],
            [12,22]
        ]
]
for A in array:
    ans = solu.solve(A[0],A[1])
    print("output for ",A," is ",ans)

# python3 advance/live/day_49/q2.py