# 가장 기초적인 배열 탐색은 for 문을 이용한 탐색

# 배열 내 최댓값 찾기

arr = [1, 2, 4, 6, 1, 2, 3]
max_value = float("-inf")
# print(max_value)

for ele in arr:
    if ele > max_value:
        max_value = ele

print(max_value)  ## 출력: 6


# 함수 콜백: 함수를 정의하는 과정에서 다른 함수를 인자로 받을 수 있음.(다른 함수를 '콜백')
# 인자로 들어가는 함수 "콜백 함수" (콜백 되는 함수)


# 다른 함수를 인자로 받는 함수 선언
def simulation(func, n):
    return func(n)


# 콜백 함수로 사용될 함수 2개 선언
def square(n):
    return n * n


def minus_one(n):
    return n - 1


print(simulation(square, 10))  # 출력: 100
print(simulation(minus_one, 10))  # 출력: 9

# 내장 함수 map, sorted
# map(함수명, iterable)  ** iterable의 인자 하나하나에 함수를 적용한다
# sorted(iterable, key = 함수명)

## 반복문을 쓸 필요가 없어진다
arr = ["1", "3", "7", "10", "33"]
res = list(map(int, arr))  # arr의 원소 각각에 int 함수를 적용한다
print(res)  # 출력: [1, 3, 7, 10, 33]


# 배열의 원소가 100이 넘으면 -1, 안 넘으면 그대로 두자

arr = [1, 201, 44, 33, 2, 105]


def overHundred(n):
    if n > 100:
        return -1
    else:
        return 1


lst = list(map(overHundred, arr))
print(lst)  # 출력: [1, -1, 1, 1, 1, -1]
lstLambda = list(map(lambda x: -1 if x > 100 else 1, arr))
print(lstLambda)  # lambda의 if-else
# lambda는 iterable의 원소 하나하나에 대해 이름 없는 함수를 적용시키는 것.


# sorted 함수 복습
setNumbers = (8, 3, 9, 1, 5)
ascNumbers = sorted(setNumbers)
print("오름차순으로 정렬된 리스트: ", ascNumbers)

dscNumbers = sorted(setNumbers, reverse=True)
print("내림차순으로 정렬된 리스트: ", dscNumbers)


# 이름, 점수, 리스트 받아 zip & 리스트로 변환 후, 점수를 내림차순으로 sort
l1 = ["Amy", "Cam", "Bob"]
l2 = [81, 62, 79]
zipped = list(zip(l1, l2))
print(zipped)  ## 출력: [('Amy', 81), ('Cam', 62), ('Bob', 79)]
print(
    sorted(zipped)
)  ## 출력: [('Amy', 81), ('Bob', 79), ('Cam', 62)] - 기준을 명시하지 않으면 묵시적으로 사전식 정렬


def standard(tup):
    return tup[1]


print(
    sorted(zipped, key=standard)
)  # 출력 - 1번 인덱스 기준으로 오름차순 정렬: [('Cam', 62), ('Bob', 79), ('Amy', 81)]
print(
    sorted(zipped, key=standard, reverse=True)
)  # 출력 - 1번 인덱스 기준으로 내림차순 정렬: [('Amy', 81), ('Bob', 79), ('Cam', 62)]
# sorted(iterable, key = 함수)의 의미:
# iterable의 원소 하나하나를 함수의 인자로 넣어 기준을 정하고, 이에 맞게 정렬


# 람다함수
# 일반적인 함수의 정의 방식
# 입력만 있다. 내부 실행은 딱히 없고 반환이 있다.
# 대개 이름을 갖지 않으나 이름을 붙일 수는 있다. 그래서 이름 없는 함수라고 불린다.


def my_sum(a, b):
    return a + b


print(my_sum(1, 2))

x = lambda a, b: a + b
print(x(1, 2))

# map() 함수의 인자(콜백함수)로 람다함수 쓰기
# 리스트 입력받아 각 리스트의 원소 제곱한 리스트 반환하기
input_l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(map(lambda i: i * i, input_l))
print(result)  # 출력: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# 이름, 점수, 리스트 받아 zip & 리스트로 변환 후, 점수 내림차순으로 sort
arr = [("Amy", 81), ("Cam", 62), ("Bob", 79)]
isFlag = True
print(
    sorted(arr, key=lambda x: x[1])
)  # 출력 - 1번 인덱스 기준으로 오름차순 정렬: [('Cam', 62), ('Bob', 79), ('Amy', 81)]
print(sorted(arr, key=lambda x: x[1] if isFlag == False else x[0]))
# 출력 - 이렇게 lambda 함수에 조건식도 걸 수 있다: [('Amy', 81), ('Bob', 79), ('Cam', 62)]
