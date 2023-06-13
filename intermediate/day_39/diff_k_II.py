from collections import Counter

class Solution:
     # @param A : tuple of integers
     # @param B : integer
     # @return a list of integers
     def diff(self, A, B):
        if B == 0:
            counts = Counter(A)
            for num, count in counts.items():
                if count > 1:
                    return 1
            return 0

        seen = set()

        for num in A:
            if num - B in seen or num + B in seen:
                return 1
            seen.add(num)

        return 0
     def diff1(self, A, B):
        n = len(A)
        hashMap = {}
        ans = []
        for i in range(n):
            k = B + A[i]
            if k not in hashMap:
                if A[i] not in hashMap:
                    hashMap[A[i]] = i
            else:
                ans.append([hashMap[k] + 1,i + 1])
        # print(ans)
        if len(ans) > 0:
            return 1
        return 0


if __name__ == "__main__":
    #  A = [2, 7, 11, 15]
    #  B = 9
    #  A = [4,7,-4,2,2,2,3,-5,-3,9,-4,9,-7,7,-1,9,9,4,1,-4,-2,3,-3,-5,4,-7,7,9,-4,4,-8]
    #  B = -3
    #  A = [1,5,3]
    #  B = 2
    #  A = [77,28,19,21,67,15,53,25,82,52,8,94,50,30,37,39,9,43,35,48,82,53,16,20,13,95,18,67,77,12,93,0]
    #  B = 53
    #  A = [53,0]
    #  B = 53
     # expected 1
    #  A = [34,63,64,38,65,83,50,44,18,34,71,80,22,28,20,96,33,70,0,25,64,96,18,2,53,100,24,47,98,69,60,55,8,38,72,94,18,68,0,53,18,30,86,55,13,93,15,43,73,68,29]
    #  B = 97
    #  expected 0
     A = [1, 5, 4, 1, 2]
     B = 0
    #  expected 0
     sol = Solution()
     ans = sol.diff(A,B)
     print(ans)