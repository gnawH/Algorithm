import sys
input = sys.stdin.readline
n = int(input())
line = list(map(int, input().split()))
line.sort()

for i in range(n):
    line[i] *= (n-i)

print(sum(line))