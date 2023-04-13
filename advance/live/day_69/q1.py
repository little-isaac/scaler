"""
Given Arr[n] first n-1 elements are sorted, sort the entire array

"""
class Solution:
    def solve(self,A):
        n = len(A)
        for i in range(n-1,0,-1):
            if A[i] < A[i-1]:
                A[i],A[i-1] = A[i-1],A[i]
        return A

# solu = Solution()
# array = [
#     [] , 
# ]
# for A in array:
#     ans = solu.solve(A[0],A[1])
#     print("output for ",A," is ",ans)

