"""
Problem Description
You are given a string A of size N consisting of lowercase alphabets.

You can change at most B characters in the given string to any other lowercase alphabet such that the number of distinct characters in the string is minimized.

Find the minimum number of distinct characters in the resulting string.



Problem Constraints
1 <= N <= 100000

0 <= B < N



Input Format
The first argument is a string A.

The second argument is an integer B.



Output Format
Return an integer denoting the minimum number of distinct characters in the string.



Example Input
A = "abcabbccd"
B = 3



Example Output
2



Example Explanation
We can change both 'a' and one 'd' into 'b'.So the new string becomes "bbcbbbccb".
So the minimum number of distinct character will be 2.
"""

class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self,A,B):
        return self.appOne(A,B)
    def appTwo(A,B):
        n = len(A)
        arr = [0]*26
        ans = 0
        for i in A:
            arr[ord(i)-97] += 1
            if(arr[ord(i)-97] == 1):
                ans += 1
        arr.sort()
        for i in range(26):
            if(B-arr[i] >= 0 and arr[i] != 0):
                ans -= 1
                B -= arr[i]
        return ans
    def appOne(self, A, B):
        if B == 0:
            return len(A)
        chars = [0] * 26
        A = list(A)
        n = len(A)
        for i in range(n):
            ele = A[i]
            aci = ord(ele)
            index = aci - 65 - 32
            chars[index] += 1
        ans = 0
        charsLen = len(chars)
        chars.sort()
        for i in range(len(chars)):
            if chars[i] == 0:
                charsLen -= 1
                continue
            if chars[i] <= B:
                # print(B,chars[i],charsLen - ans)
                B = B - chars[i]
                ans += 1
            else:
                B = 0
            if B <= 0:
                break
        return charsLen - ans



solu = Solution()
array = [
    ["abcabbccd",3] , # 2
    ["umeaylnlfd",1] , # 8
    ["hq",0] , # 2
    ["qghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvsrtkjprepggxrpnrvystmwcysyycqpevikeffmznimkkasvwsrenzkycxfxtlsgypsfadpooefxzbcoejuvpvaboygpoeylfpbnpljvrvipyamyehwqnqrqpmxujjloovaowuxwhmsncbxcoksfzkvatxdknlyjyhfixjswnkkufnuxxzrzbmnmgqooketlyhnkoaugzqrcddiuteiojwayyzpvscmpsajlfvgubfaaovlzylntrkdcpwsrtesjwhdizcobzcnfwlqijtvdwvxhrcbldvgylwgbusbmborxtlhcsmpxohgmgnkeufdxotogbgxpeyanfetcukepzshkljugggekjdqzjenpevqgxiepjsrdzjazujllchhbfqmkimwzobiwybxduunfsksrsrtekmq",119] , # 18
]
for A in array:
    ans = solu.solve(A[0],A[1])
    print("output for ",A," is ",ans)