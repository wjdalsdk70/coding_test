from collections import deque
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
degree = [0 for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

q = deque()
result = []

for i in range(1, N+1):
    if degree[i] == 0:
        q.append(i)

while (q):
    n = q.popleft()
    result.append(n)
    for next in graph[n]:
        degree[next] -= 1
        if degree[next] == 0:
            q.append(next)
print(*result)
