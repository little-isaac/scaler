class Solution:
    # @param A : string
    # @param B : list of list of integers
    # @return a list of integers
    def rangeSum(self, l, r, pf):
        if l == 0:
            return pf[r]
        else:
            return pf[r] - pf[l-1]
    def isVowel(self,char):
        return char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'

    def solve(self, A, B):
        n = len(A)
        m = len(B)
        pf = [0] * n
        ans = [0] * m
        if self.isVowel(A[0]):
            pf[0] = 1
        for i in range(1,n):
            incr = 0
            if self.isVowel(A[i]):
                incr = 1
            pf[i] = pf[i-1] + incr
        for i in range(m):
            s = B[i][0]
            e = B[i][1]
            ans[i] = self.rangeSum(s,e,pf)
        return ans

solu = Solution()
array = [
    ["scaler",[[0,2],[2,4]]], # [1,2]
    ["interviewbit",[[0,4],[9,10]]] #[2,1]
]
for A in array:
    ans = solu.solve(A[0],A[1])
    print("output for ",A," is ",ans)