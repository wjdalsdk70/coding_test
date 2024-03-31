from collections import deque
m, n, h = map(int, input().split())
data = []
tomato = []
for i in range(h):
    d = []
    for j in range(n):
        d.append(list(map(int, input().split())))
        for k in range(m):
            if d[j][k] == 1:
                tomato.append((i, j, k, 0))
    data.append(d)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]


def bfs():
    q = deque(tomato)
    max_cnt = 0
    while (q):
        z, x, y, cnt = q.popleft()
        visited[z][x][y] = True
        max_cnt = max(max_cnt, cnt)
        # print(z, x, y, cnt)
        for i in range(6):
            nx, ny, nz = x + dx[i], y+dy[i], z+dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                # print(nz, nx, ny)
                # print(data[nz][nx][ny], visited[nz][nx][ny])
                if data[nz][nx][ny] == 0 and not visited[nz][nx][ny]:
                    visited[nz][nx][ny] = True
                    q.append((nz, nx, ny, cnt + 1))
    return max_cnt


mt = bfs()

notAll = False

for i in range(h):
    for j in range(n):
        for k in range(m):
            if data[i][j][k] == 0 and not visited[i][j][k]:
                notAll = True
if len(tomato) == n*m*h:
    print(0)
elif notAll:
    print(-1)
else:
    print(mt)
