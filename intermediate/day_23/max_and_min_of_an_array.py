"""
Problem Description

Write a program to print maximum and minimum elements of the input array A of size N where you have to take integer N and other N elements as input from the user.
"""

"""
Problem Constraints

1 <= N <= 1000

1 <= A <= 1000
"""

"""
Input Format

A single line representing N followed by N integers of the array A
"""

"""
Output Format

A single line containing two space separated integers representing maximum and minimum elements of the input array.
"""

"""
Example Input

Input 1:

5 1 2 3 4 5

Output 1:

5 1
"""

"""
Input 2:

4 10 50 40 80

Output 2:

80 10
"""

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    line = input().strip()
    # line = "5 1 2 3 4 5"
    # line = "4 10 50 40 80"
    n = line.split()[0]
    arr = list(map(int, line.split()[1:]))
    min = arr[0]
    max = arr[1]
    for ele in arr:
        if min > ele:
            min = ele
        if max < ele:
            max = ele
    print(str(max),str(min))
    return 0

if __name__ == '__main__':
    main()