"""
Find LPS of the given string
Longest prefix suffix

Length of the longest prefix which is also a suffix
except full string

"""
class Solution:
    def solve(self,str):
        n = len(str)
        lps = [0] * n
        lps[0] = 0
        i = 0
        j = 1

        for i in range(1,n):
            k = lps[i-1]
            while str[k] != str[i]:
                if k == 0:
                    k = k - 1
                    break
                k = lps[k-1]
            lps[i] = k + 1
        return lps
# solu = Solution()
# array = [
#     [] , 
# ]
# for A in array:
#     ans = solu.solve(A[0],A[1])
#     print("output for ",A," is ",ans)

