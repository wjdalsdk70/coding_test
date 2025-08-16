MOD = 1_000_000_000

N = int(input().strip())

dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(N+1)]

for d in range(1, 10):
    dp[1][d][1 << d] = 1
    
for length in range(1, N):
    for digit in range(10):
        for mask in range(1 << 10):
            if dp[length][digit][mask] == 0:
                continue
            cur = dp[length][digit][mask]
            
            if digit > 0:
                dp[length+1][digit-1][mask | (1 << (digit-1))] = \
                    (dp[length+1][digit-1][mask | (1 << (digit-1))] + cur) % MOD

            if digit < 9:
                dp[length+1][digit+1][mask | (1 << (digit+1))] = \
                    (dp[length+1][digit+1][mask | (1 << (digit+1))] + cur) % MOD
                
                
