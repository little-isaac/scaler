"""
Give N distinct sorted elements,
Check if there exists a pair (i,j)
such that

A[i]-A[j] = K
K >= 0
i != j

"""
class Solution:
    def solve(self, A, K):
        n = len(A)
        p1 = 0
        p2 = 1
        while p2 < n:
            if A[p2] - A[p1] == K:
                return True
            elif A[p2] - A[p1] > K:
                p1 = p1 + 1
                if p1 == p2:
                    p2 = p2 + 1
            else:
                p2 = p2 + 1
        return False


# solu = Solution()
# array = [
#     [] , 
# ]
# for A in array:
#     ans = solu.solve(A[0],A[1])
#     print("output for ",A," is ",ans)

