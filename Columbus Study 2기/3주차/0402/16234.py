# from collections import deque
# n, l, r = map(int, input().split())
# data = []
# for _ in range(n):
#     data.append(list(map(int, input().split())))

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]


# def bfs(a, b):
#     q = deque([(a, b)])
#     country = [(a, b)]
#     visited = [[False] * n for _ in range(n)]
#     visited[a][b] = True
#     sum = data[a][b]
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
#                 if l <= abs(data[nx][ny] - data[x][y]) <= r:
#                     visited[nx][ny] = True
#                     sum += data[nx][ny]
#                     country.append((nx, ny))
#                     q.append((nx, ny))

#     # print(*country)
#     if len(country) > 1:
#         c_num = sum//len(country)
#         # print(c_num)
#         for x, y in country:
#             data[x][y] = c_num
#         return 1
#     return 0


# count = 0

# for i in range(n):
#     for j in range(n):
#         count += bfs(i, j)

# print(count)

from collections import deque

n, l, r = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * n for _ in range(n)]


def bfs(x, y):
    q = deque([(x, y)])
    temp = []
    temp.append((x, y))
    sum = data[x][y]
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(data[x][y] - data[nx][ny]) <= r:
                    q.append((nx, ny))
                    temp.append((nx, ny))
                    sum += data[nx][ny]
                    visited[nx][ny] = True
    for x, y in temp:
        data[x][y] = sum // len(temp)
    return len(temp)


def process():
    global visited
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j) > 1:
                    count += 1
    return count


days = 0
while True:
    if process() == 0:
        break
    days += 1

print(days)
