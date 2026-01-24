n = int(input())
boxes = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    max_case = 0
    for j in range(i-1, -1, -1):
        if boxes[j] < boxes[i]:
            max_case = max(max_case, dp[j])
    if max_case == 0:
        continue
    else:
        dp[i] = max_case + 1

print(max(dp))