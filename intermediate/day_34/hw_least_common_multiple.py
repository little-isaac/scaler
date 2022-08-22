"""
Problem Description
Write a program to input an integer T and then for each test case input two integers A and B in two different lines and then print T lines containing Least Common Multiple (LCM) of two given 2 numbers A and B.

LCM of two integers is the smallest positive integer divisible by both.



Problem Constraints
1 <= T <= 1000

1 <= A,B <= 1000



Input Format
In first-line input T which means number of test cases.

Next 2T lines contains input A and B for each testcase.
First line of each testcase contain an integer A and second line of the testcase contains input B.



Output Format


T lines each containing an integer representing LCM of A & B.



Example Input
Input 1:
3
2
3
9
6
2
6


Example Output
Output 1:
6
18
6


Example Explanation
Explanation:

 In first testcase 6 is the smallest positive integer which is divisible by both 2 (2 * 3 = 6) and 3 (3 * 2 = 6).
 In second testcase 18 is the smallest positive integer which is divisible by both 9 (9 * 2 = 18) and 6 (6 * 3 = 18).
 In third testcase  6 is the smallest positive integer which is divisible by both 2 (2 * 3 = 6) and 6 (6 * 1 = 6).
"""

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    T = int(input().strip())
    for i in range(T):
        A = int(input().strip())
        B = int(input().strip())
        c = 1
        while c % A != 0 or c % B != 0:
            c += 1
        print(c)
    return 0

if __name__ == '__main__':
    main()