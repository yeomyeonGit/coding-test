n, m = map(int, input().split())
lst = list(map(int, input().split()))

answer = [ i for i in lst if i < m]
print(*answer)