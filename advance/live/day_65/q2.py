"""
Given 2D array, denoting points on a 2D plane,
Return total no of distinct points in the array

"""
class Solution:

    def solve(self, A):
        n = len(A)
        hashMap = {}
        for i in range(n):
            ele = str(A[i][0]) + "#" + str(A[i][1])
            if ele in hashMap:
                hashMap[ele] = hashMap[ele] + 1
            else:
                hashMap[ele] = 1
        ans = len(hashMap)
        return ans

solu = Solution()
array = [
    [
        [
            [5,6],
            [2,8],
            [-1,-1],
            [2,-3],
            [2,8],
            [7,7],
            [2,8],
            [2,-3]
        ]
    ] , # 5
]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)

# python3 advance/live/day_65/q1.py