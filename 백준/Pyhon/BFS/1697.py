from collections import deque
N, K = map(int, input().split())
visited = [False]*100001

mv = [1,  0, 0]
mv2 = [0, 1, -1]


def bfs():
    q = deque([(N, 0)])
    visited[N] = True
    cnt = 0

    while (q):
        x, c = q.popleft()
        visited[x] = True
        if x == K:
            cnt = c
            break
        for i in range(3):
            dx = x + x*mv[i] + mv2[i]
            if (0 <= dx and dx <= 100000 and not visited[dx]):
                visited[dx] = True
                q.append((dx, c+1))

    return cnt


print(bfs())
