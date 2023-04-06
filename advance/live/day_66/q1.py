"""
Sum of n natural numbers

"""
class Solution:
    def solve(self, n):
        if n <= 1:
            return n
        else:
            return self.solve(n-1) + n

# solu = Solution()
# array = [
#     [2] , #  3
#     [3] , #  6
#     [8] , #  36
#     [4] , #  36
# ]
# for A in array:
#     ans = solu.solve(A[0])
#     print("output for ",A," is ",ans)

