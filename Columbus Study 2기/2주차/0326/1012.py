# T = int(input())

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]


# def bfs(x, y):
#     q = [(x, y)]
#     data[x][y] = 0

#     while (q):
#         x, y = q.pop(0)

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= M or ny < 0 or ny >= N:
#                 continue

#             if data[nx][ny] == 1:
#                 q.append((nx, ny))
#                 data[nx][ny] = 0


# for _ in range(T):
#     count = 0
#     M, N, K = map(int, input().split())
#     data = [[0]*N for _ in range(M)]

#     for _ in range(K):
#         x, y = map(int, input().split())
#         data[x][y] = 1

#     for i in range(M):
#         for j in range(N):
#             if data[i][j] == 1:
#                 bfs(i, j)
#                 count += 1

#     print(count)
import sys
sys.setrecursionlimit(10000)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < M) and (0 <= ny < N):
            if data[nx][ny] == 1:
                data[nx][ny] = -1
                dfs(nx, ny)


T = int(input())
for _ in range(T):
    count = 0
    M, N, K = map(int, input().split())
    data = [[0 for _ in range(N)] for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        data[x][y] = 1

    for i in range(M):
        for j in range(N):
            if data[i][j] == 1:
                dfs(i, j)
                count += 1
    print(count)
