def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    for i in range(1,N+1):
        A = int(input())
        divisors = []
        total = A * -1
        isLastStep = False
        counter =  0
        while isLastStep is False:
            counter = counter + 1
            temp = A / counter
            print("total = ",total," counter = ",counter," temp = ",temp)
            if counter > temp:
                break
            if A % counter == 0:
                divisors.extend([counter,temp])
                total = total + temp + counter
        if total == A:
            print("YES")
        else:
            print("NO")

    return 0

if __name__ == '__main__':
    main()