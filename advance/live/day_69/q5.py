"""
Given arr[n] elements & 3 indices s,m,e

"""
class Solution:
    def merge(self,A, s1, e1, e2):
        n = e1+1
        m = e2+1
        p1 = s1
        p2 = e1+1
        C = [0] * (e2-s1+1)
        k = 0

        while p1 < n and p2 < m:
            if A[p1] < A[p2]:
                C[k] = A[p1]
                p1 = p1 + 1
                k = k + 1
            else:
                C[k] = A[p2]
                p2 = p2 + 1
                k = k + 1
        while p1 < n:
            C[k] = A[p1]
            p1 = p1 + 1
            k = k + 1
        while p2 < m:
            C[k] = A[p2]
            p2 = p2 + 1
            k = k + 1
        for i in range(len(C)):
            A[i+s1] = C[i]

    def solve(self,A, s1, e1, e2):
        self.merge(A,s1, e1, e2)
        return A

# solu = Solution()
# array = [
#     [] , 
# ]
# for A in array:
#     ans = solu.solve(A[0],A[1])
#     print("output for ",A," is ",ans)

