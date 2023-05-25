"""
First non repeating character from string
# if no non repeating
"""
from collections import deque
class Solution:
    def solve(self, A):
        n = len(A)
        ans = []
        q = deque()
        hashMap = {}
        q.append(A[0])
        ans.append(A[0])
        hashMap[A[0]] = 1
        for i in range(1,n):
            ele = A[i]
            if ele in hashMap:
                hashMap[ele] = hashMap[ele] + 1
            else:
                hashMap[ele] = 1
                q.append(ele)
            while len(q) > 0 and hashMap[q[0]] != 1:
                q.popleft()
            if len(q) == 0:
                ans.append("#")
            else:
                ans.append(q[0])
        return ''.join(ans)



if __name__ == "__main__":
    solu = Solution()
    array = [
        ["abadbc"], # aabbdd
        ["abcabc"], # aaabc#
        ["abaab"], # aabb#
        ["jyhrchjyw"], # jjjjjjyrr
        ["aac"], # a#c
        ["abbacb"], # aaa#cc
    ]
    for A in array:
        ans = solu.solve(A[0])
        print("output for ",A," is ",ans)

