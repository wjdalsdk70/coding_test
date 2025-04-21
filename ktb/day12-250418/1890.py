# from collections import deque

# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# count = 0

# dx = [0, 1]
# dy = [1, 0]

# def bfs(x, y):
#     q = deque((x, y))
#     x, y = q.pop()
#     for i in range(2):
#         nx = x + arr[x][y]*dx[i]
#         ny = y + arr[x][y]*dy[i]
#         if 0 <= nx and nx < n and 0 <= ny and ny < n:
#             q.append
#             bfs(nx, ny)

# bfs(0, 0)
# print(count)

from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
count = 0
dp = [ [0]*n for _ in range(n)]
q = deque(0, 0)

while()