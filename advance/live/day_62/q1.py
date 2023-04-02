"""
longest_subarray_with_sum_0
constraints 

1<= n <= 10^5
1<= arr[i] <= 10^9

"""

class Solution:

    def prefixSum(self,A):
        n = len(A)
        pf = [0] * n
        pf[0] = A[0]
        for i in range(1,n):
            pf[i] = pf[i-1] + A[i]
        return pf
    def ifPrefixSum0(self, i,ans):
        if i+1 > ans:
            ans = i+1
        return ans
    def ifPrefixSumPresentInHashMap(self, newIndex,oldIndex,ans):
        length = newIndex - oldIndex
        if length > ans:
            ans = length
        return ans
    def solve(self, A):
        n = len(A)
        pfSum = self.prefixSum(A)
        hashMap = {}
        ans = 0
        for i in range(n):
            if pfSum[i] == 0:
                ans = self.ifPrefixSum0(i, ans)
            if pfSum[i] in hashMap:
                ans = self.ifPrefixSumPresentInHashMap(i,hashMap[pfSum[i]],ans)
            else:
                hashMap[pfSum[i]] = i
        return ans

# solu = Solution()
# array = [
#     [[3,3,4,-5,-2,2,1,-3,3,-1,5,-4,-1]] , # 10
#     [[4,-3,-1,2,-2]] , # 2
# ]
# for A in array:
#     ans = solu.solve(A[0])
#     print("output for ",A," is ",ans)

# python3 advance/live/day_62/q1.py