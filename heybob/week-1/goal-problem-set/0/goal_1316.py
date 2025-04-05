# https://www.acmicpc.net/problem/1316
# 모르겠음

# break를 깜빡
# isGroup 플래그


# 1회
"""n = int(input())
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

print(number)"""

# 2회
n = int(input())
words = [input() for _ in range(n)]
number = 0

for word in words:
    prev = word[0]
    before = []
    isGroup = True

    for i in range(len(word)):
        if word[i] != prev:
            if word[i] in before:
                isGroup = False
                break
            else:
                before.append(prev)
                prev = word[i]

    if isGroup:
        number += 1

print(number)
