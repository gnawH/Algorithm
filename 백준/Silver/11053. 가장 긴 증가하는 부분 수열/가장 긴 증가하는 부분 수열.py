N = int(input())
A = list(map(int, input().split()))

# dp[i] : i번째 인덱스까지 가장 긴 증가하는 수열의 길이
dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))