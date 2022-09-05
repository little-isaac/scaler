def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n = int(input().strip())
    # n = 4
    for i in range(n):
        # Top Left * printing
        for j in range(i,n):
            print("*",end="")

        # Top Left ' ' printing
        for j in range(0,i):
            print(" ",end="")

        # Top right ' ' printing
        for j in range(0,i):
            print(" ",end="")

        # Top right '*' printing
        for j in range(i,n):
            print("*",end="")
        print("")
    for i in range(n):

        # Bottom left '*' printing
        for j in range(0,i+1):
            print("*",end="")

        # Bottom left ' ' printing
        for j in range(i+1,n):
            print(" ",end="")

        # Bottom right ' ' printing
        for j in range(i+1,n):
            print(" ",end="")

        # Bottom right '*' printing
        for j in range(0,i+1):
            print("*",end="")
        print("")
    return 0

if __name__ == '__main__':
    main()