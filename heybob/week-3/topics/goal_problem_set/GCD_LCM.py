# TODO: 유클리드 호제법을 이용한 GCD 함수 작성
# https://blogshine.tistory.com/112


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


a, b = map(int, input().split())
print(gcd(a, b))
print(int((a * b) / gcd(a, b)))
