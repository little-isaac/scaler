"""
Given 2 sorted arrays, A[n], B[m]
create C[] which contains overall the sorted data
"""
class Solution:
    def solve(self,A, B):
        n = len(A)
        m = len(B)
        C = []
        p1 = 0
        p2 = 0
        while p1 < n and p2 < m:
            if A[p1] < B[p2]:
                C.append(A[p1])
                p1 = p1 + 1
            else:
                C.append(B[p2])
                p2 = p2 + 1
        
        while p1 < n:
            C.append(A[p1])
            p1 = p1 + 1
        while p2 < m:
            C.append(B[p2])
            p2 = p2 + 1
        return C

# solu = Solution()
# array = [
#     [] , 
# ]
# for A in array:
#     ans = solu.solve(A[0],A[1])
#     print("output for ",A," is ",ans)

