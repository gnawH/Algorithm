import sys
input = sys.stdin.readline
n = int(input())
waste = 1000 - n
count = 0

while waste != 0:
    if waste >= 500:
        count += (waste // 500)
        waste = waste % 500
    elif waste >= 100:
        count += (waste // 100)
        waste = waste % 100
    elif waste >= 50:
        count += (waste // 50)
        waste = waste % 50
    elif waste >= 10:
        count += (waste // 10)
        waste = waste % 10
    elif waste >= 5:
        count += (waste // 5)
        waste = waste % 5
    else:
        count += (waste // 1)
        waste = waste % 1

print(count)