n = int(input())
ary = list(map(int, input().split()))
d = [0] * 100
# d = 각 창고를 고려할 때, 각 창고까지 도달할 때에 최적으로 터는 법. 최적해를 저장하고 새로운 최적해가 발생할 때마다 갱신하게 됨.

d[0] = 1
d[1] = 3

for i in range(2, n):
    d[i] = max(d[i - 2] + ary[i], d[i - 1])
    print(d[i])

print(d[n - 1])
