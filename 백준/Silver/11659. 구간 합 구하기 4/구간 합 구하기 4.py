# 슬라이싱 (시간초과, O(n^2))
'''
n, m = map(int, input().split())
num = list(map(int, input().split()))

for i in range(m):
    i, j = map(int, input().split())
    print(sum(num[i-1:j]))
'''

# 구간 합 알고리즘 (누적 합)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
sum = [0]
tmp = 0

# 누적 합 (O(n))
for a in num:
    tmp += a
    sum.append(tmp)

# 구간 합
for k in range(m):
    i, j = map(int, input().split())
    print(sum[j] - sum[i-1])