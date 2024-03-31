n, m = map(int, input().split())
edges = [[] for _ in range(n+1)]
count = [n+1] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    edges[b].append(a)


def dfs(i):
    if count[i] != n+1:
        return count[i]
    count[i] = 0
    for edge in edges[i]:
        count[i] += 1+dfs(edge)
    return count[i]


for v in range(1, n+1):
    count[v] = dfs(v)

max_value = max(count)
# # 최대값과 동일한 모든 요소를 찾습니다.
max_elements = [i for i in range(1, n+1) if count[i] == max_value]

print(' '.join(list(map(str, max_elements))))
