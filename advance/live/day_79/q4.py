"""
3 closest sum
Find 3 integer in array A such that its sum is closest to B 
return the sum of these 3 integers

Note - there is only one possible solution
"""
class Solution:
    def solve(self, A, B):
        n = len(A)
        A.sort()
        bS = float("-inf")
        bD = abs(B - bS)
        d = bD
        for i in range(n-2):
            j = i + 1
            k = n -1
            sum = A[i] + A[j] + A[k]
            d = abs(B - sum)
            while j < k:
                if sum == B:
                    return sum
                if d < bD:
                    bS = sum
                if sum < B:
                    j = j + 1
                else:
                    k = k - 1
        return bS

# solu = Solution()
# array = [
#     [] , 
# ]
# for A in array:
#     ans = solu.solve(A[0],A[1])
#     print("output for ",A," is ",ans)

