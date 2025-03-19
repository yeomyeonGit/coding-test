# 피보나치 수열 소스코드(재귀적)
# 탑다운(메모이제이션) 방식은 재귀함수를 사용한다.
# '하향식'이라고도 한다.

# 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수를 재귀함수로 구현(탑다운 프로그래밍)
def fibo(x):
    # 종료 조건(1 혹은 2일 때 1을 반환)

    print('f(' + str(x) + ')', end= ' ')
    if x == 1 or x == 2:
        # d[x] = 1
        return 1

    # 이미 계산한 적 있는 문제라면 계산했던 값을 반환
    if d[x] != 0:      # 피보나치 수열은 0 값이 될 수 없으니까
        return d[x]
    
    # 계산한 적 없는 문제라면 계산해서 기록하기
    d[x] = fibo(x - 1) + fibo(x - 2)

    # print(d)
    return d[x]

print(fibo(8))
print(d)



# 8번째 수까지만 구해서 쭉 늘어놓음