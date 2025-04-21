from collections import deque

n = int(input())
homes = [ list(map(int, input().strip())) for _ in range(n)]
visited = [ [False]*n for _ in range(n)]
results = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j):
    going = deque([(i, j)])
    count = 1
    visited[i][j] = True
    homes[i][j] = -1
    while(going):
        x, y = going.pop()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and not visited[xx][yy] and homes[xx][yy]:
                going.append((xx, yy))
                count += 1
                visited[xx][yy] = True
                homes[xx][yy] = -1
    return count

total = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j] and homes[i][j] == 1:
            results.append(bfs(i, j))

print(len(results))
for result in results:
    print(result)