from collections import deque
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(n):
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(i)

    return 1


count = 0

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)
