n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
results = []
used = [0] * n

def dfs(total, count):
    if total > k:
        return
    if total == k:
        results.append(count)
        return
    for i in range(n):
        dfs(total + coins[i], count + 1)

dfs(0, 0)
print(min(results) if results else -1)