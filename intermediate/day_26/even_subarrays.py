"""
Problem Description
You are given an integer array A.

Decide whether it is possible to divide the array into one or more subarrays of even length such that the first and last element of all subarrays will be even.

Return "YES" if it is possible; otherwise, return "NO" (without quotes).



Problem Constraints
1 <= |A|, A[i] <= 106



Input Format
The first and the only input argument is an integer array, A.



Output Format
Return a string "YES" or "NO" denoting the answer.



Example Input
Input 1:

 A = [2, 4, 8, 6]
Input 2:

 A = [2, 4, 8, 7, 6]


Example Output
Output 1:

 "YES"
Output 2:

 "NO"


Example Explanation
Explanation 1:

 We can divide A into [2, 4] and [8, 6].
Explanation 2:

 There is no way to divide the array into even length subarrays.

 Note - From My End.

Whole array is subarray of it self.
if array size is not even we cannot divide it into even size subaray.
if array size is even and first and last element is even
  then only we can divide it into subarray with first and last element with even element.
  so this problem is very simple.
"""

class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        n = len(A)
        if A[0] % 2 == 0 and A[n-1] % 2 == 0 and n % 2 == 0:
            return "YES"
        return "NO"



solu = Solution()
array = [
    [2, 4, 8, 6], # YES
    [2, 4, 8, 7, 6],  # NO
    # [1,2,4,6,8], # NO
    # [2,1,4,8,3,6] # YES
    # [ 978, 847, 95, 729, 778, 586, 188, 782, 813, 870, 871, 940, 312, 693, 580, 101, 760, 837, 564, 633, 680, 155, 241, 374, 682, 290, 850, 601, 433, 922, 773, 959, 530, 290, 990, 50, 516, 409, 868, 131, 664, 851, 721, 880, 20, 450, 745, 387, 787, 823, 392, 242, 674, 347, 65, 135, 819, 324, 651, 678, 139, 940 ] # YES
]
for A in array:
    ans = solu.solve(A)
    print("output for ",A," is ",ans)