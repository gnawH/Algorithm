# 인덱스 접근 (시간초과, O(n^3))
'''
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]

for i in range(m):
    sum = 0
    x1, y1, x2, y2 = map(int, input().split())
    
    for i in range(y1-1, y2):
        for j in range(x1-1, x2):
            sum += arr[i][j]
    print(sum)
'''

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
sum_arr = [[0] * (n+1) for i in range(n+1)]

# 누적 합
for i in range(1, n+1):
    for j in range(1, n+1):
        sum_arr[i][j] = sum_arr[i-1][j] + sum_arr[i][j-1] - sum_arr[i-1][j-1] + arr[i-1][j-1]

# 구간 합
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(sum_arr[x2][y2] - sum_arr[x1-1][y2] - sum_arr[x2][y1-1] + sum_arr[x1-1][y1-1])