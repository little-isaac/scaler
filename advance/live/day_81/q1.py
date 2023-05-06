"""
Longest subscrting with all distinct characters

"""
class Solution:
    def solve(self,S):
        n = len(S)
        A = list(S)
        uniq = {}
        i = 0
        j = 0
        ans = 0
        while j < n:
            if A[j] in uniq:
                del uniq[A[i]]
                i = i + 1
            else:
                uniq[A[j]] = j
                j = j + 1
            ans = max(ans, len(uniq))
        return ans

# solu = Solution()
# array = [
#     [] , 
# ]
# for A in array:
#     ans = solu.solve(A[0],A[1])
#     print("output for ",A," is ",ans)

