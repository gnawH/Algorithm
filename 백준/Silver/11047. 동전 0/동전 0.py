import sys
input = sys.stdin.readline
n, k = map(int, input().split())
worth = [int(input()) for i in range(n)]
cnt = 0

while k != 0:
    value = worth.pop()
    if value <= k:
        cnt += (k // value)
        k = k % value
print(cnt)