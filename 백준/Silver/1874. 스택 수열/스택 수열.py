import sys
input = sys.stdin.readline
n = int(input())
cnt = 1
stack = []
result = []

for i in range(n):
    num = int(input())
    while num >= cnt:
        stack.append(cnt)
        result.append('+')
        cnt += 1
    if stack[-1] == num:
        result.append('-')
        stack.pop()
    else:
        print('NO')
        exit()
for i in result:
    print(i)