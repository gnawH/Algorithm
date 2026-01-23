n = int(input())

dp = [0] * (n+1)    # 수를 만들 때 필요한 제곱수 개수

dp[1] = 1

for i in range(2, n+1):
    min_num = 5
    for j in range(1, int(i**0.5)+1):
        min_num = min(min_num, dp[i-(j**2)])
    dp[i] = min_num + 1
print(dp[n])