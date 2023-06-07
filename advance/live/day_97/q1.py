"""

Path from root to given node
"""
class Solution:
    path = []
    def check(self, root, k):
        if root is None:
            return False
        if root.data == k:
            return True
        return self.check(root.left, k) or self.check(root.right, k)
    def findPath(self, root, k):
        if root is None:
            return False
        if root.data == k:
            self.path.append(root)
            return True
        if self.check(root.left, k) or self.check(root.right, k):
            self.path.append(root)
            return True
        return False
    def solve(self):
        pass

if __name__ == "__main__":
    solu = Solution()
    array = [
        [] ,
    ]
    for A in array:
        ans = solu.solve(A[0],A[1])
        print("output for ",A," is ",ans)
# solu = Solution()
# array = [
#     [] , 
# ]
# for A in array:
#     ans = solu.solve(A[0],A[1])
#     print("output for ",A," is ",ans)

