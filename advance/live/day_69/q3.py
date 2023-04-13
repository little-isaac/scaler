"""
Bubble Sort

"""
class Solution:
    def solve(self,A):
        n = len(A)
        for i in range(n-1):
            for j in range(n-i-1):
                if A[j] > A[j+1]:
                    A[j],A[j+1] = A[j+1],A[j]
        return A

# solu = Solution()
# array = [
#     [] , 
# ]
# for A in array:
#     ans = solu.solve(A[0],A[1])
#     print("output for ",A," is ",ans)

