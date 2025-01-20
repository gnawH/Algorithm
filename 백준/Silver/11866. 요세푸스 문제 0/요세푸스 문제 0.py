import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
deq = deque([i for i in range(1, N+1)])
result = []

while len(deq) != 0:
    deq.rotate(-(K-1))
    result.append(deq.popleft())

print("<" + ", ".join(map(str, result)) + ">")