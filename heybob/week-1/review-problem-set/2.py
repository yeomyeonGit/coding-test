# 📝 복습 문제 2: N 이하 짝수 제곱수 리스트 반환하는 함수 제작
# 문제 설명
# 정수 N을 입력받아, N 이하의 숫자 중에서 짝수만을 제곱하여 리스트를 만들어 반환하는 함수를 정의하시오.

# 예시

# 입력: N = 5
# 출력: [4, 16]
# 입력: N = 10
# 출력: [4, 16, 36, 64, 100]

number = int(input())


def isEven(number):
    result = []
    for i in range(1, number + 1):
        if i % 2 == 0:
            result.append(i * i)

    return result


print(isEven(number))
