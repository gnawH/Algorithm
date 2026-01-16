N = int(input()) # 1 ~ 300
stairs = [int(input()) for _ in range(N)] # 1 ~ 10,000

dp = [0] * N    # 0 ~ N-1 번째 계단까지 최대점수 배열 선언 및 초기화
dp[0] = stairs[0]

if N == 1:  # 계단이 1개인 Case
    print(dp[0])
elif N == 2:    # 계단이 2개인 Case
    dp[1] = stairs[0] + stairs[1]
    print(dp[-1])
else:   # 계단이 3개 이상인 Case
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
    for i in range(3, N):
        dp[i] = max(stairs[i] + dp[i-2], stairs[i] + stairs[i-1] + dp[i-3])
    print(dp[-1])