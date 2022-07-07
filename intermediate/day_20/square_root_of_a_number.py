class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        isFound = False
        first = 1
        last = A
        ans = -1
        if A == 1:
            return 1
        while isFound is False:
            center = int((first + last) / 2)
            if first == center or last == center:
                isFound = True
                ans = -1
                break
            if center * center == A:
                isFound = True
                ans = center
                break
            elif center * center > A:
                last = center
                first = 1
            elif center * center < A:
                first = center
                last = last
        return ans


solu = Solution()
array = [1]
for A in array:
    ans = solu.solve(A)
    print("output for ",A," is ",ans)
