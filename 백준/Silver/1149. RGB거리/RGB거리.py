N = int(input())

dp = [[0] * 3 for _ in range(N)]
paint = []

for test_case in range(N):
    paint.append(list(map(int, input().split())))


dp[0][0], dp[0][1], dp[0][2] = paint[0][0], paint[0][1], paint[0][2]

for i in range(1, N):
    dp[i][0] = min(paint[i][0] + dp[i-1][1], paint[i][0] + dp[i-1][2])
    dp[i][1] = min(paint[i][1] + dp[i-1][0], paint[i][1] + dp[i-1][2])
    dp[i][2] = min(paint[i][2] + dp[i-1][0], paint[i][2] + dp[i-1][1])

print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))