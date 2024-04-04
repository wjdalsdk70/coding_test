from collections import deque
t = int(input())

dx = [-2, -2, -1, -1, +2, +2, 1, +1]
dy = [-1, +1, -2, +2, -1, +1, -2, +2]


def bfs(l, a, b, c, d):
    q = deque([(a, b, 0)])
    visited = [[False]*l for _ in range(l)]
    visited[a][b] = True
    min_cnt = 0

    while (q):
        x, y, cnt = q.popleft()
        if x == c and y == d:
            min_cnt = cnt
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, cnt + 1))

    return min_cnt


data = []
for _ in range(t):
    ll = int(input())
    s_x, s_y = map(int, input().split())
    t_x, t_y = map(int, input().split())
    print(bfs(ll, s_x, s_y, t_x, t_y))
