n = int(input())

tmp = []
for _ in range(n):
    name, score = map(str, input().split())
    tmp.append((name, int(score)))

tmp = sorted(tmp, key = lambda x: x[1])

for i in tmp:
    print(i[0], end = " ")
