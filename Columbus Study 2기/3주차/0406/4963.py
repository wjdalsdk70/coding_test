from collections import deque
data = []
visited = []
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def bfs(a, b):
    q = deque([(a, b)])
    visited[a][b] = True

    while (q):
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if data[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))


while (1):
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    data = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False]*w for _ in range(h)]
    count = 0

    for i in range(h):
        for j in range(w):
            if data[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                count += 1
    print(count)
