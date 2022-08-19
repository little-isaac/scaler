"""
Construct a class called Matrix which stores a 2D Array. It should store

The number of rows

The number of columns

The 2D Array itself

Implement the following functionalities inside this class :-

input() -> Reads the input from the user. This method should read the input from the user and populate the entire array. Each row will be in a new line and all the elements in a row will be space-separated.

add(Matrix) -> Returns the sum of two matrices. Assume the matrices provided have the same dimensions.

subtract(Matrix) -> Returns the sum of two matrices. Assume the matrices provided have the same dimensions.

transpose() -> Returns a new matrix containing the transpose of the given original matrix.

print() -> prints the entire matrix row by row. Each row will be in a new line and values in each row should be separated by a single space.

You may define any properties in the class as you see appropriate.
"""

class Matrix:
    # Define properties here
    rows = 0
    columns = 0
    mat = [[]]
    # Define constructor here
    def __init__(self,r,c) -> None:
        self.rows = r
        self.columns = c
        self.mat = [[0] * c for _ in range(r)]

    def input(self):
        # Complete the function
        for i in range(self.rows):
            self.mat[i] = list(map(int, input().strip().split()))
    def add(self, x: "Matrix") -> "Matrix":
        # Complete the function
        n = self.rows
        m = self.columns
        ans = Matrix(n,m)
        for i in range(n):
            for j in range(m):
                ans.mat[i][j] = self.mat[i][j] + x.mat[i][j]
        return ans

    def subtract(self, x: "Matrix") -> "Matrix":
        # Complete the function
        n = self.rows
        m = self.columns
        ans = Matrix(n,m)
        for i in range(n):
            for j in range(m):
                ans.mat[i][j] = self.mat[i][j] - x.mat[i][j]
        return ans

    def transpose(self) -> "Matrix":
        # Complete the function
        n = self.rows
        m = self.columns
        ans = Matrix(m,n)
        for i in range(n):
            for j in range(m):
                ans.mat[j][i] = self.mat[i][j]
        return ans

    def print(self):
        # Complete the function
        n = self.rows
        m = self.columns
        for i in range(n):
            for j in range(m):
                print(self.mat[i][j],end=" ")
            print("")

# Matrix a = new Matrix(10, 5)  // 10 rows, 5 columns
# a.input() 
# Matrix b = new Matrix(10, 5)  // 10 rows, 5 columns
# b.input()
# Matrix c1 = a.add(b)
# Matrix c2 = a.subtract(b)
# Matrix c3 = a.transpose()
# a.print()