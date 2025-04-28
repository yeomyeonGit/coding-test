numberLst = [list(map(int, input().split())) for _ in range(9)]

maxNum = -1
for i in range(len(numberLst)):
    for j in range(len(numberLst[i])):
        if maxNum < numberLst[i][j]:
            maxNum = numberLst[i][j]
            rowNum = i + 1
            colNum = j + 1

print(maxNum)
print(rowNum, colNum)
