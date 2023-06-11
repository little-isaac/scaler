class Solution:
     # @param A : tuple of integers
     # @param B : integer
     # @return a list of integers
     def twoSum(self, A, B):
        n = len(A)
        hashMap = {}
        ans = []
        for i in range(n):
            k = B - A[i]
            if k not in hashMap:
                if A[i] not in hashMap:
                    hashMap[A[i]] = i
            else:
                ans.append([hashMap[k] + 1,i + 1])
        # print(ans)
        if len(ans) > 0:
            return ans[0]
        return None


if __name__ == "__main__":
    #  A = [2, 7, 11, 15]
    #  B = 9
    #  A = [4,7,-4,2,2,2,3,-5,-3,9,-4,9,-7,7,-1,9,9,4,1,-4,-2,3,-3,-5,4,-7,7,9,-4,4,-8]
    #  B = -3
     A = [-10,-10,-10]
     B = -5
     sol = Solution()
     ans = sol.twoSum(A,B)
     print(ans)