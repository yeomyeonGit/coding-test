# 📝 복습 문제 1: 문자열 길이 필터링 함수 제작
# 문제 설명
# 알파벳으로 이루어진 문자열 하나를 입력받아,
# "길이가 5 이상인 경우에만" 문자열 전체를 대문자로 변환하여 반환하는 함수를 정의하시오.
# 길이가 5 이하라면 '길이가 5 이하입니다' 메시지를 반환합니다.

# 예시

line = input()


def line_length(line):
    result = ""
    if len(line) >= 5:
        result = line.upper()

    else:
        result = "길이가 5 이하입니다."
    return result


print(line_length(line))
