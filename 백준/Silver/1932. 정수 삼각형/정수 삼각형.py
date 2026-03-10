n = int(input())

num_stair = []
dp = [[0] * n for _ in range(n)]
for _ in range(n):
    num_stair.append(list(map(int, input().split())))

dp[0][0] = num_stair[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + num_stair[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + num_stair[i][j]

print(max(dp[n-1]))