from collections import deque
n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    cnt = 0

    while (q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if data[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    cnt += 1
                    q.append((nx, ny))

    return cnt+1


count = 0
d_count = []
visited = [[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if data[i][j] and not visited[i][j]:
            count += 1
            d_count.append(bfs(i, j))

print(count)
d_count.sort()
for d in d_count:
    print(d)
