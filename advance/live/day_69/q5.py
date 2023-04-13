"""
Given arr[n] elements & 3 indices s,m,e

"""
class Solution:
    def solve(self,A, s1, e1, e2):
        n = e1+1
        m = e2+1
        p1 = s1
        p2 = e1+1
        C = []
        for i in range(p1):
            C.append(A[i])
        while p1 < n and p2 < m:
            if A[p1] < A[p2]:
                C.append(A[p1])
                p1 = p1 + 1
            else:
                C.append(A[p2])
                p2 = p2 + 1
        while p1 < n:
            C.append(A[p1])
            p1 = p1 + 1
        while p2 < m:
            C.append(A[p2])
            p2 = p2 + 1
        for i in range(e2+1,len(A),1):
            C.append(A[i])
        return C

# solu = Solution()
# array = [
#     [] , 
# ]
# for A in array:
#     ans = solu.solve(A[0],A[1])
#     print("output for ",A," is ",ans)

