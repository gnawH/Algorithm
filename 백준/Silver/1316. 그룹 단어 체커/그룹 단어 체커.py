N = int(input())

words = [input() for _ in range(N)]
result = 0

for word in words:
    word_char = set()
    tmp = ' '
    count = 0
    for character in word:
        if len(word) == 1:
            word_char.add(character)
            count += 1
            break
        elif tmp == character:
            continue
        elif character in word_char:
            count = 0
            break
        else:
            tmp = character
            word_char.add(character)
            count += 1
            continue

    if len(word_char) == count:
        result += 1

print(result)