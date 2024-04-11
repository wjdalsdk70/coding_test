T = int(input())
for _ in range(T):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0]*n for _ in range(2)]
    dp[0][0] = data[0][0]
    dp[1][0] = data[1][0]
    if n >= 2:
        dp[0][1] = data[1][0] + data[0][1]
        dp[1][1] = data[0][0] + data[1][1]

    for i in range(2, n):
        dp[0][i] = data[0][i] + max(dp[1][i-2], dp[1][i-1])
        dp[1][i] = data[1][i] + max(dp[0][i-2], dp[0][i-1])

    print(max(dp[0][n-1], dp[1][n-1]))
