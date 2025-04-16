import sys
input = sys.stdin.readline

m = input().split('-')
result = 0

for i in range(len(m)):
    sum = 0
    for j in m[i].split('+'):
        sum += int(j)
    if i == 0:
        result += sum
    else:
        result -= sum

print(result)