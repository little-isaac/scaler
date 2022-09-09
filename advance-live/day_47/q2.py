class Solution:

    def solve(self,A,Q):
        n = len(A)
        t = len(Q)
        pf = [0]*n
        for i in range(t):
            A[Q[i][0]] += Q[i][2]
            if Q[i][1] < n:
                continue
            A[Q[i][1]+1] -= Q[i][2]
            # print(A)
        pf[0] = A[0]
        for i in range(1,n):
            pf[i] = pf[i-1] + A[i]
        return pf


solu = Solution()
array = [
    [[0,0,0,0,0,0,0],[[1,3,2],[2,5,3],[2,4,-1]]],
    [[0,0,0,0,0,0,0],[[2,4,6],[3,6,2],[1,3,4]]]
    ]
for A in array:
    ans = solu.solve(A[0],A[1])
    print("output for ",A," is ",ans)
