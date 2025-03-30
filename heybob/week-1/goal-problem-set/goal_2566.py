import sys

numbers = sys.stdin.read().strip().split("\n")

# print(original)   # 줄바꿈을 기준으로 한줄씩 리스트에 넣어줬음

lines = list(map(lambda x: x.split(), numbers))
# 글자 하나씩 떼어줌

intLst = []
for line in lines:
    tmp = []
    for j in line:
        tmp.append(int(j))

    intLst.append(tmp)

# print(intLst)  # 정수형 리스트로 변환하고 하나의 리스트로 묶어줌

maximum = -99999999999
x = 0
y = 0

for i in range(len(intLst)):
    for j in range(len(intLst[0])):
        if intLst[i][j] > maximum:
            maximum = intLst[i][j]
            x = i+1
            y = j+1

print(maximum)
print(x, y)

