n = int(input())

tmp = []
for _ in range(n):
    tmp.append(int(input()))

tmp.sort(reverse=True)

for i in tmp:
    print(i, end=" ")
