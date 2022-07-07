import time
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    # N = int(input())

    st = time.time()

    # first()

    et = time.time()
    elapsed_time = round((et - st) * 1000,2)
    # print(" First ",elapsed_time, 'ms')


    st = time.time()

    second(500)

    et = time.time()
    elapsed_time = round((et - st) * 1000,2)
    print(" Second ",elapsed_time, 'ms')

    return 0

def second(A):
    totalNumberFound = 0
    isStop = False
    for a in range(0,10):
        if isStop:
            break
        a3 = a**3
        a100 = a * 100
        for b in range(0,10):
            if isStop:
                break
            b3 = b**3
            b10 = b * 10
            for c in range(0,10):
                c3 = c ** 3
                c1 = c
                a3b3c3 = a3 + b3 + c3
                number = a100 + b10 + c1
                if a3b3c3 == number:
                    print(number)
                if number > A:
                    isStop = True
                    break

def first():
    totalNumberFound = 0
    counter = 0
    while totalNumberFound != 5:
        counter = counter + 1
        total = 0
        for i in str(counter):
            cube = int(i) ** 3
            total = total + cube
        if total == counter:
            # print(counter)
            totalNumberFound = totalNumberFound + 1
if __name__ == '__main__':
    main()