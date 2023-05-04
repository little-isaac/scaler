"""
Find LPS of the given string
Longest prefix suffix

Length of the longest prefix which is also a suffix
except full string

"""
class Solution:
    def getLPS(self,str):
        arrStr = list(str)
        n = len(arrStr)
        ans = 0
        p1 = 0
        p2 = n-1
        while p1 < p2:
            if arrStr[p1] == arrStr[p2]:
                p1 = p1 + 1
                p2 = p2 - 1
                ans = ans + 1
            else:
                break
        return ans
    def solve(self,str):
        return self.getLPS(str)

# solu = Solution()
# array = [
#     [] , 
# ]
# for A in array:
#     ans = solu.solve(A[0],A[1])
#     print("output for ",A," is ",ans)

