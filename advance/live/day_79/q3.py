"""
Given N Elements Array 

A[i] represents the height of wall

return max water stored between the walls
"""
class Solution:
    def solve(self, A):
        n = len(A)
        p1 = 0
        p2 = n-1
        ans = 0
        while p1 < p2:
            ele1 = A[p1]
            ele2 = A[p2]
            minHeight = min(ele1,ele2)
            width = p2 - p1
            area = minHeight * width
            ans = max(area, ans)
            if ele1 < ele2:
                p1 = p1 + 1
            else:
                p2 = p2 - 1
        return ans

# solu = Solution()
# array = [
#     [] , 
# ]
# for A in array:
#     ans = solu.solve(A[0],A[1])
#     print("output for ",A," is ",ans)

