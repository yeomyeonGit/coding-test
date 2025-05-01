n = int(input())
words = list(input() for _ in range(n))

tmp = []
total = 0

for word in words:
    current = ""
    tmp = []
    for letter in word:
        if current != letter:
            current = letter
            if current not in tmp:
                tmp.append(current)
                isGroup = True
            else:
                isGroup = False
                break

    if isGroup == True:
        total += 1

print(total)
