import sys
input = sys.stdin.readline
n = int(input())
card = list(map(int, input().split()))
m = int(input())
num = list(map(int, input().split()))
dict = {}

for i in card:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
for j in num:
    if j in dict:
        print(dict[j], end=' ')
    else:
        print(0, end=' ')