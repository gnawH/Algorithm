n = int(input())
word = [input() for i in range(n)]

for i in range(1, 51):
    tmp = []
    for j in range(len(word)):
        if len(word[j]) == i:
            if word[j] in tmp:
                continue
            else:
                tmp.append(word[j])
    tmp.sort()
    for j in tmp:
        print(j)
        