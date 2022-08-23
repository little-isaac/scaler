"""
Problem Description
Write a recursive function that, given a string S, prints the characters of S in reverse order.



Problem Constraints
1 <= |s| <= 1000



Input Format
First line of input contains a string S.



Output Format
Print the character of the string S in reverse order.



Example Input
Input 1:

 scaleracademy
Input 2:

 cool


Example Output
Output 1:

 ymedacarelacs
Output 2:

 looc


Example Explanation
Explanation 1:

 Print the reverse of the string in a single line.
"""


"""
You can increase recursion limit using following code snippet
import sys
sys.setrecursionlimit(10**6)
"""
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    s = input().strip()
    reverseString(s,len(s)-1)
    return 0

def reverseString(s,i):
    if i <= -1:
        return
    print(s[i],end="")
    if i != 0:
        print(s[i-1],end="")
    return reverseString(s,i-2)
if __name__ == '__main__':
    main()