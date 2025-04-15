import sys
import heapq

input = sys.stdin.readline

n = int(input())
hqueue = []
total = 0

for i in range(n):
    heapq.heappush(hqueue, int(input()))

while len(hqueue) > 1:
    a = heapq.heappop(hqueue)
    b = heapq.heappop(hqueue)
    tmp = a+b
    total += tmp
    
    heapq.heappush(hqueue, tmp)
    
print(total)