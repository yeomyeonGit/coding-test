# 모음의 개수
# https://www.acmicpc.net/problem/1264

lst = []

while True:
    line = input()

    if line == '#':
        break

    else:
        lst.append(line)

print(lst)

n = 0
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for sentence in lst:
    n = 0
    for letter in sentence:
        if letter in vowels:
            n += 1
    
    print(n)