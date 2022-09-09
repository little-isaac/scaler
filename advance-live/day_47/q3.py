class Solution:

    def solve(self,A):
        n = len(A)
        pfm = []
        pfm.append(A[0])
        for i in range(1,n):
            if A[i] < pfm[i-1]:
                pfm.append(pfm[i-1])
            else:
                pfm.append(A[i])
        return pfm

solu = Solution()
array = [
    [[1,-6,3,2,8,7]], #1,1,3,3,8,8
    [[3,-2,6,2,8]], # 3,3,6,6,8
    ]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)
