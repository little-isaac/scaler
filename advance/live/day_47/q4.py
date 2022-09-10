class Solution:

    def solve(self,A):
        n = len(A)
        sfm = [0]*n
        sfm[n-1] = A[n-1]
        for i in range(n-2,-1,-1):
            if A[i] < sfm[i+1]:
                sfm[i] = sfm[i+1]
            else:
                sfm[i] = A[i]
        return sfm

solu = Solution()
array = [
    [[3,10,6,7,0,2,-1]], #10,10,7,7,2,2,-1
    ]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)
