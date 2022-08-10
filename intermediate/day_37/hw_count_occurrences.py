"""
Problem Description
Find the number of occurrences of bob in string A consisting of lowercase English alphabets.



Problem Constraints
1 <= |A| <= 1000


Input Format
The first and only argument contains the string A, consisting of lowercase English alphabets.


Output Format
Return an integer containing the answer.


Example Input
Input 1:

  "abobc"
Input 2:

  "bobob"


Example Output
Output 1:

  1
Output 2:

  2


Example Explanation
Explanation 1:

  The only occurrence is at second position.
Explanation 2:

  Bob occures at first and third position.
"""

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        A = list(A)
        n = len(A)
        ans = 0
        for i in range(n-2):
            if A[i] == 'b' and A[i+1] == 'o' and A[i+2] == 'b':
                ans += 1
        return ans


solu = Solution()
array = [
    ["abobc"] , # 1
    ["bobob"] , # 2
]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)