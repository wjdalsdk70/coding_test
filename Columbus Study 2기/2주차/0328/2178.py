from collections import deque
n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q = deque([(0, 0, 0)])
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True

    while (q):
        x, y, cnt = q.popleft()
        if x == n-1 and y == m-1:
            print(cnt+1)
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if data[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, cnt+1))


# data[nx][ny] = 0 방문처리는 메모리 초과함
bfs()
# dfs(0, 0, 0)
