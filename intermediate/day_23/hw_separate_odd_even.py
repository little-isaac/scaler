def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    T = int(input())
    for i in range(T):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        odd = []
        even = []
        for ele in arr:
            if ele % 2 == 0:
                even.append(ele)
            else:
                odd.append(ele)
        if len(odd) > 0:
            print(" ".join(map(str, odd))+" ")
        else:
            print()
        if len(even) > 0:
            print(" ".join(map(str, even))+" ")
        else:
            print()
    return 0

if __name__ == '__main__':
    main()