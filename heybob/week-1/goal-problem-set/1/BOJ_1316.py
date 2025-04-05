# 그룹 단어 체커
# https://www.acmicpc.net/problem/1316

number = int(input())

words = [input() for _ in range(number)]

n = 0

for word in words:
    isGroup = True
    lst = []
    prev = word[0]
    for letter in word:
        if letter != prev:
            if letter in lst:
                isGroup = False
                break
            else:
                lst.append(prev)
                prev = letter

    if isGroup == True:
        n += 1

print(n)
