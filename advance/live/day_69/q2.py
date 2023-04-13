"""
Insertion sort

"""
class Solution:
    def solve(self,A):
        n = len(A)
        for i in range(n-1):
            for j in range(i+1,0,-1):
                if A[j] < A[j-1]:
                    A[j],A[j-1] = A[j-1],A[j]
                else:
                    break
        return A

# solu = Solution()
# array = [
#     [] , 
# ]
# for A in array:
#     ans = solu.solve(A[0],A[1])
#     print("output for ",A," is ",ans)

