import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, sys.stdin.readlines()))
for i in sorted(num):
    print(i)