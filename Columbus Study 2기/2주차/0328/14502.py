from collections import deque
from itertools import combinations
n, m = map(int, input().split())
data = []
birus = []
safe = []
for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(m):
        if data[i][j] == 2:
            birus.append((i, j))
        elif data[i][j] == 0:
            safe.append((i, j))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, temp):
    q = deque([(x, y)])
    visited[x][y] = True

    while (q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if temp[nx][ny] == 0 and not visited[nx][ny]:
                    temp[nx][ny] = 2
                    visited[nx][ny] = True
                    q.append((nx, ny))


count = 0

for zone in combinations(safe, 3):
    temp = [row[:] for row in data]
    visited = [[False]*m for _ in range(n)]
    cnt = 0
    for x, y in zone:
        temp[x][y] = 1
    for x, y in birus:
        if not visited[x][y]:
            bfs(x, y, temp)
    for i in range(n):
        cnt += temp[i].count(0)
        # for j in range(m):
        #     if data[i][j] == 0 and not visited[i][j]:
        #         cnt += 1
    count = max(count, cnt)
    # for x, y in zone:
    #     temp[x][y] = 0

print(count)
