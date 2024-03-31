from collections import deque
M, N = map(int, input().split())
data = [[0]*M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
result = 0
data = []
for i in range(N):
    data.append(list(map(int, input().split())))
    for j in range(M):
        if data[i][j] == 1:
            q.append((0, j, i))

while (q):
    n, x, y = q.popleft()
    result = max(result, n)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= M or 0 > ny or ny >= N:
            continue

        if data[ny][nx] == 0:
            q.append((n+1, nx, ny))
            data[ny][nx] = 1

flag = True
for i in data:
    for j in i:
        if j == 0:
            flag = False
            break
if flag:
    print(result)
else:
    print(-1)

# def bfs(x, y):
#     q = [(0, x, y)]
#     data[y][x] = 1
#     n = 0

#     while (q):
#         n, x, y = q.pop(0)

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx < 0 or nx >= M or 0 > ny or ny >= N:
#                 continue

#             if data[ny][nx] == 0:
#                 q.append((n+1, nx, ny))
#                 data[ny][nx] = 1
#     return n

# for i in range(N):
#     for j in range(M):
#         if data[j][i] == 1:
#             result = max(result, bfs(j, i))

# def dfs(n, x, y):

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if (0 <= nx < M) and ((0 <= ny < N)):
#             if data[ny][nx] == 0:
#                 data[ny][nx] = 1
#                 dfs(n+1, nx, ny)
