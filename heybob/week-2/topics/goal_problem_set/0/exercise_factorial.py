# 📝 연습 문제 1: 더블 팩토리얼
# 문제 설명
# n의 더블 팩토리얼을 계산하는 재귀 함수를 작성하세요.

# 더블 팩토리얼은 주어진 수 n에 대해 n × (n−2) × (n−4) × ⋯ 1 또는 n × (n−2) × (n−4) × ⋯ 2까지의 곱을 계산하는 것입니다.

# 예를 들어, n = 5일 때 결과는 5 × 3 × 1 = 15입니다.


# TODO: 더블 팩토리얼을 계산하는 재귀 함수 작성
def double_factorial(n):
    if n <= 1:
        return 1
    else:
        return n * double_factorial(n - 2)


# 예시 출력
print(double_factorial(5))  # 출력: 15
print(double_factorial(6))  # 출력: 48
