# 📝 복습 문제 5: 리스트 변환 및 zip 함수 활용하기
# 문제 설명
# 다음과 같이 길이가 같은 사람 이름과 나이가 '공백으로 구분된 문자열'로 입력됩니다.

names = "가희 라희 나희 다희 마희"
ages = "32 22 34 54 28"

# 각 문자열을 리스트로 변환하고, ages는 정수의 리스트로 변환하세요.
nameLst = names.split()
ageLst = ages.split()

print(nameLst, ageLst)

# 리스트 컴프리헨션을 이용하여, 이름과 나이 리스트의 정보를 다음과 같은 2차원 배열로 만드세요.
# 예시 출력: [['가희', 32], ['라희', 22], ['나희', 34], ['다희', 54], ['마희', 28]]

result = [[nameLst[i], ageLst[i]] for i in range(5)]
print(result)
# print(list((zip(nameLst, ageLst))))

# zip() 함수를 이용하여, 이름과 나이 리스트의 정보를 다음과 같은 'list of tuples'로 만드세요.
# 예시 출력: [('가희', 32), ('라희', 22), ('나희', 34), ('다희', 54), ('마희', 28)]
res2 = list(zip(nameLst, ageLst))
print(res2)
