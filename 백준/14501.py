n = int(input())
data = []
dp = [0 for i in range(n+1)]
for _ in range(n):
    data.append(list(map(int, input().split())))

for i in range(n):
    for j in range(i+data[i][0], n+1):
        if dp[j] < dp[i] + data[i][1]:
            dp[j] = dp[i] + data[i][1]

print(dp[-1])
