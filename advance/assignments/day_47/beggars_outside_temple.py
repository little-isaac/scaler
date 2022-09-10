class Solution:

    def solve(self,a,Q):
        n = a
        A = [0] * a
        t = len(Q)
        pf = [0]*n
        for i in range(t):
            A[Q[i][0]-1] += Q[i][2]
            # print(i,A)
            if Q[i][1]-1 >= n-1:
                continue
            A[Q[i][1]] -= Q[i][2]
        pf[0] = A[0]
        for i in range(1,n):
            pf[i] = pf[i-1] + A[i]
        return pf


solu = Solution()
array = [
    # [[0,0,0,0,0,0,0],[[1,3,2],[2,5,3],[2,4,-1]]],
    # [[0,0,0,0,0,0,0],[[2,4,6],[3,6,2],[1,3,4]]],
    [5,[[1, 2, 10], [2, 3, 20], [2, 5, 25]]],
    [10,[[1, 3, 10],[6, 9, 2],[3, 5, 3],[2, 8, 4],[6, 7, 5]]]
    ]
for A in array:
    ans = solu.solve(A[0],A[1])
    print("output for ",A," is ",ans)
