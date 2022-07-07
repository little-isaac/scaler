def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    A = int(input())
    for i in range(1,11):
        print(A," * ",i," = ",(A*i))
    return 0

if __name__ == '__main__':
    main()