# 반복문으로 다이내믹 프로그래밍 소스코드를 작성하는 방식을 보텀업(반복문) 방식이라고 한다.
# '상향식'이라고도 한다.
# 다이내믹 프로그래밍의 전형적인 방식이다.

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 첫 번째와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

# 피보나치 함수 반복문으로 구현
for i in range(3, n + 1):
    print("f(" + str(i) + ")", end=" ")
    d[i] = d[i - 1] + d[i - 2]

print(d[4])

# 99번째까지 싹 다 구해서 4번째처럼 딱 한 지점만 골라서 값을 조회하는 형식
