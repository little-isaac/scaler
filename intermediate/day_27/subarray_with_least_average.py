class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def appOne(self, A, B):
        ans = -1
        n = len(A)
        mini = float('inf')
        for i in range((n-B)+1):
            sum = 0
            for j in range(i,i+B):
                sum = sum + A[j]
            avg = sum / B
            if avg < mini:
                mini = avg
                ans = i
        return ans
    def rangeSum(self, l, r, pf):
        if l == 0:
            return pf[r]
        else:
            return pf[r] - pf[l-1]
    def appTwo(self, A, B):
        ans = -1
        n = len(A)
        pf = [0] * n
        pf[0] = A[0]
        mini = float('inf')
        for i in range(1,n):
            pf[i] = pf[i-1] + A[i]
        for i in range((n-B)+1):
            sum = self.rangeSum(i,i+B-1,pf)
            avg = sum / B
            if avg < mini:
                mini = avg
                ans = i
        return ans
    def solve(self, A, B):
        return self.appTwo(A, B)



solu = Solution()
array = [
    [[3, 7, 90, 20, 10, 50, 40],3] , # 3
    [[3, 7, 5, 20, -10, 0, 12],2] ,  # 4
    [[ 20, 3, 13, 5, 10, 14, 8, 5, 11, 9, 1, 11 ],9] # 3
]
for A in array:
    ans = solu.solve(A[0],A[1])
    print("output for ",A," is ",ans)