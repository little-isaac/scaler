class Solution:
	# @param A : list of integers
	# @return an integer
    def bulbs(self,A):
        n = len(A)
        ans = 0
        last = A[0]

        if A[0] == 0:
            ans = ans + 1

        for i in range(1,n):
            ele = A[i]
            if last != ele:
                last = ele
                ans = ans + 1
        return ans
    def solve(self, A):
        return self.bulbs(A)

solu = Solution()
array = [
    [0, 1, 0, 1], # 4
    [1, 1, 1, 1],  # 0
    [0,0,1,0,1,0], # 5
]
for A in array:
    ans = solu.solve(A)
    print("output for ",A," is ",ans)