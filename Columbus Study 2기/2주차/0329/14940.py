from collections import deque
n, m = map(int, input().split())
data = []
tx, ty = 0, 0
for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(m):
        if data[i][j] == 2:
            tx, ty = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False]*m for _ in range(n)]


def bfs():
    q = deque([(tx, ty, 0)])
    data[tx][ty] = 0

    while (q):
        x, y, cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if data[nx][ny] == 1 and not visited[nx][ny]:
                    data[nx][ny] = cnt + 1
                    visited[nx][ny] = True
                    q.append((nx, ny, cnt + 1))


bfs()
for i in range(n):
    for j in range(m):
        if data[i][j] == 1 and not visited[i][j]:
            data[i][j] = -1
for d in data:
    print(*d)
