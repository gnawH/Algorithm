import sys
input = sys.stdin.readline
N, M = map(int, input().split())
listen = set(input().rstrip() for i in range(N))
see = set(input().rstrip() for i in range(M))
tmp = []
for i in listen:
    if i in see:
        tmp.append(i)
print(len(tmp))
tmp.sort()
for i in tmp:
    print(i)
