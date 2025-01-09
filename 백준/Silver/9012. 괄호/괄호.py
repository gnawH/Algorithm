import sys
input = sys.stdin.readline
t = int(input())

for i in range(t):
    count = 0
    tmp = 0
    isvps = input().rstrip()
    for j in isvps:
        if j == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            tmp += 1
    if tmp == 0 and count == 0:
        print('YES')
    else:
        print('NO')