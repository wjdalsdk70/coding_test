from collections import deque
N, M, K = map(int, input().split())
graph = [[0]*(M+1) for _ in range(N+1)]
visited = [[False]*(M+1) for _ in range(N+1)]


for _ in range(K):
    a, b = map(int, input().split())
    graph[a][b] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 < nx < N+1 and 0 < ny < M+1:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1
    return cnt


max_count = 0

for i in range(1, N+1):
    for j in range(1, M+1):
        if graph[i][j] == 1 and not visited[i][j]:
            max_count = max(max_count, bfs(i, j))

print(max_count)
