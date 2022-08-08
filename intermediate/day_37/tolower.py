class Solution:
    # @param A : list of characters
    # @return a list of characters
    def to_lower(self, A):
        low = ord('A')
        high = ord('Z')
        n = len(A)
        for i in range(n):
            aci = ord(A[i])
            if aci > low-1 and aci < high + 1:
                A[i] = chr(aci ^ 32)
        return A
solu = Solution()
array = [
    [['S', 'c', 'A', 'l', 'e', 'r', 'A', 'c', 'a', 'D', 'e', 'm', 'y']] , # ['s', 'c', 'a', 'l', 'e', 'r', 'a', 'c', 'a', 'd', 'e', 'm', 'y']
    [['S', 'c', 'a', 'L', 'e', 'r', '#', '2', '0', '2', '0']] , # ['s', 'c', 'a', 'l', 'e', 'r', '#', '2', '0', '2', '0']
]
for A in array:
    ans = solu.to_lower(A[0])
    print("output for ",A," is ",ans)