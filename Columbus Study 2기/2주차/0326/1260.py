from collections import deque
N, M, S = map(int, input().split())
edges = [[] for _ in range(N+1)]
visited = [False]*(N+1)
result = []

for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)


def dfs(node):
    visited[node] = True  # 현재 노드를 방문 처리합니다.
    result.append(node)  # 방문하는 노드를 출력합니다.
    edges[node].sort()

    for next_node in edges[node]:
        if not visited[next_node]:
            dfs(next_node)  # 인접 노드에 대해 재귀적으로 함수 호출


def bfs():
    q = deque()
    q.append(S)
    result.append(S)
    visited[S] = True
    while q:
        node = q.popleft()
        edges[node].sort()
        for edge in edges[node]:
            if not visited[edge]:
                result.append(edge)
                visited[edge] = True
                q.append(edge)


dfs(S)
print(*result)
result = []
visited = [False]*(N+1)
bfs()
print(*result)
