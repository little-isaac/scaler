def runTheFunction(n):
    count1 = 0
    count2 = 0
    for i in range(3, int(n/3), 3):
        count1 = count1 + 1
        for j in range(2, int(n/2), 2):
            count2 = count2 + 1
            # print(str(i),str(j))
        # print("inner loop for ",str(i),str(count2))

    print(str(n),str(count1), " - ",int(count2/count1), " - ",count1 * count2)


arr = [100,150,200,250,300,350,400,450,500,550,6600,650,700,750,800,850,900,950,1000]
for i in arr:
    runTheFunction(i)