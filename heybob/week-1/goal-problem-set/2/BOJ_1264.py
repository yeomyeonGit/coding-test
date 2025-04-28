lines = []
line = ""

while True:
    line = input()
    if line == "#":
        break
    else:
        lines.append(line)

for each in lines:
    n = 0
    for j in range(len(each)):
        if each[j] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            n += 1
    print(n)