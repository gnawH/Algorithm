import sys
T = int(sys.stdin.readline())
dp = [0] * 41

for _ in range(T):
    N = int(sys.stdin.readline())
    dp[1] = 1
    for i in range(2, N + 1):
        dp[i] = dp[i-1] + dp[i-2]
    if N == 0:
        print(1, 0)
    else:
        print(dp[N-1], dp[N])