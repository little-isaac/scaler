class Solution:
    # @param A : list of characters
    # @return a list of characters
    def to_upper(self, A):
        low = ord('a')
        high = ord('z')
        n = len(A)
        for i in range(n):
            aci = ord(A[i])
            if aci > low-1 and aci < high + 1:
                A[i] = chr(aci ^ 32)
        return A
solu = Solution()
array = [
    [['S', 'c', 'A', 'L', 'E', 'r', 'A', 'c', 'a', 'D', 'e', 'm', 'y']] , # ['S', 'C', 'A', 'L', 'E', 'R', 'A', 'C', 'A', 'D', 'E', 'M', 'Y']
    [['S', 'c', 'a', 'L', 'e', 'R', '#', '2', '0', '2', '0']] , # ['S', 'C', 'A', 'L', 'E', 'R', '#', '2', '0', '2', '0']
]
for A in array:
    ans = solu.to_upper(A[0])
    print("output for ",A," is ",ans)