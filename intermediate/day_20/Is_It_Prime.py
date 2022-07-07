def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    A = int(input())
    isLastStep = False
    counter =  1
    while isLastStep is False:
        counter = counter + 1
        temp = A / counter
        if counter > temp:
            break
        if A % counter == 0 and counter != A:
            print("NO")
            return 0
    print("YES")
    return 0

if __name__ == '__main__':
    main()