# strInout = "2 4 2\n1 2 3\n1 3 4"
# strInout = "2 3 4\n1 2 3\n3 1 2 2 2\n2 1 2\n4 1 2 2 3"
# strInout = "8 9 20\n2 5 6\n1 6 5\n3 1 5 4 6\n2 8 6\n2 2 2\n3 4 4 2 8\n1 9 4\n2 7 4\n1 2 2\n3 2 8 3 6\n3 1 5 7 4\n2 5 3\n3 6 6 5 5\n4 8 3 2 8\n3 5 3 5 4\n2 1 5\n4 2 9 2 9\n1 4 2\n3 6 1 3 1\n3 8 7 3 2"

"""
8 9 20
2 5 6
1 6 5
3 1 5 4 6
2 8 6
2 2 2
3 4 4 2 8
1 9 4
2 7 4
1 2 2
3 2 8 3 6
3 1 5 7 4
2 5 3
3 6 6 5 5
4 8 3 2 8
3 5 3 5 4
2 1 5
4 2 9 2 9
1 4 2
3 6 1 3 1
3 8 7 3 2

"""

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    # inputVar = strInout.split("\n")
    # firstIn = inputVar[0].strip().split(" ")
    firstIn = input().strip().split(" ")
    N = int(firstIn[0])
    M = int(firstIn[1])
    Q = int(firstIn[2])
    # print(N,M,Q)
    cSwap = [-1]*M
    rSwap = [-1]*N
    for j in range(M):
        cSwap[j] = j
    for i in range(N):
        rSwap[i] = i
    # print("row",rSwap)
    # mat = [[0]* M for _ in range(N)]
    # mat = []
    # print(getNumber(1,0,3))
    # counter = 1
    # for i in range(N):
    #     temp = []
        # for j in range(M):
    #         temp.append(counter)
            # mat[i][j] = counter
            # counter += 1
    #     mat.append(temp)
    # printMat(mat)
    for q in range(1,Q+1):
        # secIn = inputVar[q].strip().split(" ")
        secIn = input().strip().split(" ")
        a = int(secIn[0])
        if a == 1:
            c1 = int(secIn[1]) -1
            c2 = int(secIn[2]) -1
            cSwap[c1],cSwap[c2] = cSwap[c2],cSwap[c1]
            # for i in range(N):
                # mat[i][c1],mat[i][c2] = mat[i][c2],mat[i][c1]
            # print(a,c1,c2)
            # printMat(mat)
        elif a == 2:
            r1 = int(secIn[1]) -1
            r2 = int(secIn[2]) -1
            rSwap[r1],rSwap[r2] = rSwap[r2],rSwap[r1]
            # for j in range(M):
                # mat[r1][j],mat[r2][j] = mat[r2][j],mat[r1][j]
            # print(a,r1,r2)
            # printMat(mat)
        elif a == 3:
            x1 = int(secIn[1]) -1
            y1 = int(secIn[2]) -1
            x2 = int(secIn[3]) -1
            y2 = int(secIn[4]) -1
            if rSwap[x1] != -1:
                x1 = rSwap[x1]
            if rSwap[x2] != -1:
                x2 = rSwap[x2]
            if cSwap[y1] != -1:
                y1 = cSwap[y1]
            if cSwap[y2] != -1:
                y2 = cSwap[y2]
            print(getNumber(x1,y1,M) | getNumber(x2,y2,M))
            # print(mat[x1][y1] | mat[x2][y2])
            # printMat(mat)
        elif a == 4:
            x1 = int(secIn[1]) -1
            y1 = int(secIn[2]) -1
            x2 = int(secIn[3]) -1
            y2 = int(secIn[4]) -1
            if rSwap[x1] != -1:
                x1 = rSwap[x1]
            if rSwap[x2] != -1:
                x2 = rSwap[x2]
            if cSwap[y1] != -1:
                y1 = cSwap[y1]
            if cSwap[y2] != -1:
                y2 = cSwap[y2]
            print(getNumber(x1,y1,M) & getNumber(x2,y2,M))
            # print(mat[x1][y1] & mat[x2][y2])
            # printMat(mat)
    # print("col",cSwap)
    # print("row",rSwap)
    return 0
def getNumber(r,c,m):
    return ((r+1)*m) - (m-(c+1))
def printMat(a):
    print()
    for i in a:
        print("[ ",end="")
        for j in i:
            print(j, end=' ')
        print("]",end="")
        print()
if __name__ == '__main__':
    main()