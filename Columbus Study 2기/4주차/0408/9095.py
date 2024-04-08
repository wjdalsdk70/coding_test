T = int(input())

dp = {}
dp[1] = 1
dp[2] = 2
dp[3] = 4


def dpf(i):
    if i in dp.keys():
        return dp[i]

    dp[i] = dpf(i-3) + dpf(i-2) + dpf(i-1)
    return dp[i]


for _ in range(T):
    N = int(input())
    print(dpf(N))
