MOD = 1_000_000_000

N = int(input().strip())

dp = [[0] * 10 for _ in range(N+1)]

for d in range(1, 10):
    dp[1][d] = 1

for l in range(2, N+1):
    for d in range(10):
        if d > 0:
            dp[l][d] += dp[l-1][d-1]
        if d < 9:
            dp[l][d] += dp[l-1][d+1]
        dp[l][d] %= MOD

print(sum(dp[N]) % MOD)