"""
Given an array, calculate no of distinct elements in every subarray of size K

Sliding window with the hashMap

"""


class Solution:

    def solve(self, A, k):
        n = len(A)
        ans = []
        hashSet = {}
        for i in range(k):
            ele = A[i]
            if ele in hashSet:
                hashSet[A[i]] = hashSet[A[i]] + 1
            else:
                hashSet[A[i]] = 1
        ans.append(len(hashSet))
        start = 1
        end = k
        while end < n:
            print(start,end)
            oldEle = A[start-1]
            freq = hashSet[oldEle]
            if freq == 1:
                del hashSet[oldEle]
            else:
                hashSet[oldEle] = hashSet[oldEle] - 1

            newEle = A[end]
            if newEle in hashSet:
                hashSet[newEle] = hashSet[newEle] + 1
            else:
                hashSet[newEle] = 1
            ans.append(len(hashSet))
            start = start + 1
            end = end + 1
        return ans

solu = Solution()
array = [
    [[2,4,3,8,3,9,4,9],4] , #  [4,3,3,4,3]
]
for A in array:
    ans = solu.solve(A[0],A[1])
    print("output for ",A," is ",ans)

# python3 advance/live/day_65/q1.py