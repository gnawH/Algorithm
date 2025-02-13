word = input()
dict = {}
cnt = 0

for i in word.upper():
    dict[i] = 0

for i in word.upper():
    dict[i] += 1

for k, v in dict.items():
    if max(dict.values()) == v:
        tmp = k
        cnt += 1

if cnt >= 2:
    print('?')

else:
    print(tmp)
    