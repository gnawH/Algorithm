import sys
input = sys.stdin.readline
n = int(input())
list = []

for i in range(n):
    x, y = map(int, input().split())
    list.append([x, y])

for i in list:
    cnt = 0
    for j in range(n):
        if i[0] < list[j][0] and i[1] < list[j][1]:
            cnt += 1
    cnt += 1
    print(cnt, end=" ")