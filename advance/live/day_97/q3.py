"""

nodes at a distance k from given node below the node.



"""
class Solution:
    def countNodesBelow(self,src,k):
        if src is None:
            return 0
        if k == 0:
            return 1
        return self.countNodesBelow(src.left, k - 1) + self.countNodesBelow(src.right, k - 1)
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

