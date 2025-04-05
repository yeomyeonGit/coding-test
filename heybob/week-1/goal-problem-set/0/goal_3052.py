# https://www.acmicpc.net/problem/3052

# lst = list(map(int, input()) for _ in range(10))

lst = [int(input()) for _ in range(10)]

answerLst = []
for number in lst:
    answerLst.append(number % 42)

print(len(set(answerLst)))