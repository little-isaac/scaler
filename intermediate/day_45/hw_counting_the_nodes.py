"""
Problem Description
Given the root of a tree A with each node having a certain value, find the count of nodes with more value than all its ancestor.



Problem Constraints
1 <= Number of Nodes <= 200000

1 <= Value of Nodes <= 2000000000



Input Format
The first and only argument of input is a tree node.



Output Format
Return a single integer denoting the count of nodes that have more value than all of its ancestors.



Example Input
Input 1:

 
     3
Input 2:

 
    4
   / \
  5   2
     / \
    3   6


Example Output
Output 1:

 1 
Output 2:

 3


Example Explanation
Explanation 1:

 There's only one node in the tree that is the valid node.
Explanation 2:

 The valid nodes are 4, 5 and 6.
"""
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def countNodes(self, A, parentNode):
        if A is None:
            return 0
        isCount = 0
        if parentNode is None or A.val > parentNode.val:
            parentNode = A
            isCount += 1
        return isCount + self.countNodes(A.left,parentNode) + self.countNodes(A.right,parentNode)
    def solve(self, A):
        return self.countNodes(A,None)