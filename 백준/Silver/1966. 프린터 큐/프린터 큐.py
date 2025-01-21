import sys
from collections import deque

input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    N, M = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    cnt = 1

    while queue:
        if queue[0] == max(queue):
            if M == 0:
                print(cnt)
                break
            queue.popleft()
            cnt += 1
            M -= 1
        else:
            queue.rotate(-1)
            M = (M - 1) % len(queue)
