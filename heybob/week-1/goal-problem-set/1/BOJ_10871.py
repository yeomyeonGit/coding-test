# X보다 작은 수
# https://www.acmicpc.net/problem/10871

n, x = map(int, input().split())

numbers = list(map(int, input().split()))

lst = [i for i in numbers if i < x]

print(*lst)
