from collections import deque
k = int(input())
w, h = map(int, input().split())
data = []
for i in range(h):
    data.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0, -2, -2, -1, -1, +2, +2, 1, +1]
dy = [0, 0, -1, 1, -1, +1, -2, +2, -1, +1, -2, +2]

visited = [[False]*w for _ in range(h)]


def bfs():
    q = deque([(0, 0, 0, 0)])
    visited[0][0] = True
    min_cnt = 1000000

    while (q):
        x, y, cnt, kt = q.popleft()
        print(x, y, cnt, kt)
        if x == h-1 and y == w-1:
            min_cnt = min(min_cnt, cnt)
        for i in range(12):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if data[nx][ny] == 0 and not visited[nx][ny]:
                    if i >= 4:
                        if kt == k:
                            break
                    visited[nx][ny] = True
                    q.append((nx, ny, cnt + 1, kt+1))

    return min_cnt


# result = bfs()
# if result:
#     print(result)
# else:
#     print(-1)

# # GPT의 도움

k = int(input())
w, h = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(h)]

dx = [-1, 1, 0, 0, -2, -2, -1, -1, +2, +2, 1, +1]
dy = [0, 0, -1, 1, -1, +1, -2, +2, -1, +1, -2, +2]

visited = [[[False] * (k + 1) for _ in range(w)] for _ in range(h)]


def bfs():
    q = deque([(0, 0, 0, 0)])  # x, y, cnt, k 사용 횟수
    visited[0][0][0] = True
    while q:
        x, y, cnt, kt = q.popleft()
        if x == h - 1 and y == w - 1:
            return cnt
        for i in range(12):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and data[nx][ny] == 0:
                next_kt = kt + 1 if i >= 4 else kt
                if next_kt <= k and not visited[nx][ny][next_kt]:
                    visited[nx][ny][next_kt] = True
                    q.append((nx, ny, cnt + 1, next_kt))
    return -1


print(bfs())
