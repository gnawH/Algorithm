import sys
input = sys.stdin.readline
n = int(input())
que = []

for i in range(n):
    order = input()
    if 'push' in order:
        a, b = order.split()
        que.append(b)
    if 'pop' in order:
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
            que.remove(que[0])
    if 'size' in order:
        print(len(que))
    if 'empty' in order:
        if len(que) == 0:
            print(1)
        else:
            print(0)
    if 'front' in order:
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    if 'back' in order:
        if len(que) == 0:
            print(-1)
        else:
            print(que[len(que)-1])