n = input()
result = []
for i in n:
    result.append(int(i))

reverse = ''
for i in sorted(result, reverse=True):
    reverse += str(i)

print(reverse)