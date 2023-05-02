"""
Given n distinct sorted element, 
check if there exists a pair(i,j) such that a[i] + a[j], i != j

"""
class Solution:
    def solve(self, A, K):
        n = len(A)
        p1 = 0
        p2 = n-1
        while p1 < p2:
            p1Ele = A[p1]
            p2Ele = A[p2]
            sum = p1Ele + p2Ele
            if sum == K:
                return True
            elif sum > K:
                p2 = p2 - 1
            else:
                p1 = p1 + 1
        return False


# solu = Solution()
# array = [
#     [] , 
# ]
# for A in array:
#     ans = solu.solve(A[0],A[1])
#     print("output for ",A," is ",ans)

