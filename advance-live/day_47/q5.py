class Solution:
    def getPFM(self,A):
        n = len(A)
        pfm = []
        pfm.append(A[0])
        for i in range(1,n):
            if A[i] < pfm[i-1]:
                pfm.append(pfm[i-1])
            else:
                pfm.append(A[i])
        return pfm
    def getSFM(self,A):
        n = len(A)
        sfm = [0]*n
        sfm[n-1] = A[n-1]
        for i in range(n-2,-1,-1):
            if A[i] < sfm[i+1]:
                sfm[i] = sfm[i+1]
            else:
                sfm[i] = A[i]
        return sfm

    def solve(self,A):
        n = len(A)
        pfm = self.getPFM(A)
        sfm = self.getSFM(A)
        ans = 0
        for i in range(1,n-1):
            leftMax = pfm[i-1]
            rightMax = sfm[i+1]
            level = min(leftMax,rightMax)
            # if the m is small then A[i] then it means we cannot store water
            # print(i,A[i],level,level-A[i])
            diff = level-A[i]
            if diff > 0:
                ans += diff
        return ans

solu = Solution()
array = [
    [[2,1,3,2,1,2,4,3,2,1,3,1]], # 8
    [[10,7,3,5,2,3,6,9,8,11]], # 37
    [[4,2,5,7,4,2,3,6,8,2,3]], # 16
    ]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)
