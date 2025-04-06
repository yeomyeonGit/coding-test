def decimal_to_binary(decimal):
    if decimal // 2 == 0:
        return str(decimal % 2)

    deciBi = decimal_to_binary(decimal // 2)

    current_Bi = str(decimal % 2)

    result = deciBi + current_Bi

    return result


print(decimal_to_binary(14))

while True:
    print("10진수를 입력하세요.")
    decimal = int(input())

    if decimal < 0:
        break

    print(decimal_to_binary(decimal))
