"""
Given an array of non-negative, 
arrange them in such a way that they form the largets number.

return the ans as a string, since the result can be very large
"""
from functools import cmp_to_key

class Solution:

    def compare(self,a,b):
        s1 = str(a)
        s2 = str(b)
        if s1 + s2 > s2 + s1:
            return -1
        else:
            return 1
    def solve(self, A):
        A.sort(key=cmp_to_key(self.compare))
        return "".join(map(str,A))

# solu = Solution()
# array = [
#     [] , 
# ]
# for A in array:
#     ans = solu.solve(A[0],A[1])
#     print("output for ",A," is ",ans)

