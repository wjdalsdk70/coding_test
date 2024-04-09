N = int(input())
dp = [-1]*1000001

dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, N+1):
    a, b, c = 1000001, 1000001, 1000001
    if i % 3 == 0:
        a = dp[int(i/3)]
    if i % 2 == 0:
        b = dp[int(i/2)]

    c = dp[i] = dp[i-1]
    dp[i] = min(a, b, c) + 1

print(dp[N])
