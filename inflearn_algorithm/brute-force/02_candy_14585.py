# 링크: https://www.acmicpc.net/problem/14568

n = int(input())

cnt = 0
for A in range(n+1):
    for B in range(n+1):
        for C in range(n+1):
            if A + B + C == n:
                if C >= B + 2:
                    if A != 0 and B != 0 and C != 0:
                        if A % 2 != 1:
                            cnt += 1
                print(A, B, C)

print(cnt)

