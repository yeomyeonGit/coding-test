# 모음의 개수
# https://www.acmicpc.net/problem/1264

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
sentences = []
while True:
    line = input()

    if line == '#':
        break
    else:
        sentences.append(line)

# print(sentences)


for sentence in sentences:
    number = 0
    for letter in sentence:
        if letter in vowels:
            number += 1
        
    print(number)

    # else:
    #     number = 0
    #     for letter in line:
    #         if letter in vowels:
    #             number += 1
