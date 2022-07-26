class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):


solu = Solution()
array = [
    [9, 17] , # YES
    [1] ,  # NO
]
for A in array:
    ans = solu.solve(A[0],A[1])
    print("output for ",A," is ",ans)