import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
list = [i for i in range(1, n+1)]
qlist = deque(list)

for i in range(n):
    if len(qlist) == 1:
        print(qlist[0])
        break
    else:
        qlist.popleft()
        qlist.rotate(-1)