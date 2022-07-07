"""
Problem Statement

Given an integer array A of size N and an integer B.
You have to print the same array after rotating it B times towards the right.
"""

"""
Problem Constraints

1 <= N <= 10^6
1 <= A[i] <=10^8
1 <= B <= 10^9

"""

"""
Input Format

There are 2 lines in the input

Line 1: The first number is the size N of the array A. Then N numbers follow which indicate the elements in the array A.

Line 2: A single integer B.

"""

"""
Output Format
Print array A after rotating it B times towards the right.
"""

"""
Example Input
Input 1 :
4 1 2 3 4
2
"""
"""
Example Output
Output 1 :
3 4 1 2
"""

"""
Example Explanation
Example 1 :

N = 4, A = [1, 2, 3, 4] and B = 2.

Rotate towards the right 2 times - [1, 2, 3, 4] => [4, 1, 2, 3] => [3, 4, 1, 2]

Final array = [3, 4, 1, 2]

"""

def replaceArray(arr,s,e):
    i = s
    j = e
    while(i<j):
        arr[i],arr[j] = arr[j],arr[i]
        i = i + 1
        j = j - 1
    return arr

def replaceArrayNTimes(arr,b):
    l = len(arr)

    b = b % l

    arr = replaceArray(arr,0,l-1)

    arr = replaceArray(arr,0,b-1)

    arr = replaceArray(arr,b,l-1)

    return arr

firstLine = input().strip()
secondLine = int(input().strip())

# firstLine = "4 1 2 3 4"
# secondLine = int("2")

n = firstLine.split()[0]
array = list(map(int, firstLine.split()[1:]))


print(" ".join(map(str,replaceArrayNTimes(array,secondLine))))