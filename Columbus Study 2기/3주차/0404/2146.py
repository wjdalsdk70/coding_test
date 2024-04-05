from collections import deque
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
eg = [[]]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, n):
    q = deque([(x, y)])
    visited[x][y] = True
    data[x][y] = n
    e = []

    while (q):
        is_eg = False
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if data[nx][ny] == 0:
                    is_eg = True
                if not visited[nx][ny] and data[nx][ny] != 0:
                    visited[nx][ny] = True
                    data[nx][ny] = n
                    q.append((nx, ny))
        if is_eg:
            e.append((x, y))
    eg.append(e)


cnt = 1

for i in range(N):
    for j in range(N):
        if data[i][j] != 0 and not visited[i][j]:
            bfs(i, j, cnt)
            cnt += 1

# print(*data)
# print(*eg)


def bfs2(a, b, n):
    q = deque([(a, b, 0)])
    visited2 = [[False]*N for _ in range(N)]
    visited2[a][b] = True

    while (q):
        x, y, cnt = q.popleft()

        if data[x][y] != 0 and data[x][y] != n:
            return cnt-1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited2[nx][ny] and data[nx][ny] != n:
                    visited2[nx][ny] = True
                    q.append((nx, ny, cnt+1))

    return 10000


min_b = 10000

for i in range(1, cnt):
    for a, b in eg[i]:
        min_b = min(bfs2(a, b, i), min_b)

print(min_b)
