# https://www.acmicpc.net/problem/1316
# 모르겠음

# break를 깜빡


import sys

n = int(input())
lst = [input() for _ in range(n)]
number = 0

for word in lst:
    prev = word[0]
    arr = []
    isGroup = True

    for j in range(len(word)):
        if prev != word[j]:
            arr.append(prev)
            prev = word[j]
            
        if word[j] in arr:
            isGroup = False
            break

    if isGroup:
        number += 1
    
    # print(word, j, isGroup )

print(number)

            
            
        #     if lst[i][j] in arr:
        #     continue
        # else:

            # prev = lst[i][j]
            # arr.append(lst[i][j])
             
        
    


