N = int(input())

dp = [0] * max(4, N+1)   # 최소 길이 4 확보
dp[1], dp[2], dp[3] = 1, 2, 1

for i in range(4, N+1):
    if dp[i-1] == 1 or dp[i-3] == 1:
        dp[i] = 2
    else:
        dp[i] = 1

print("SK" if dp[N] == 1 else "CY")