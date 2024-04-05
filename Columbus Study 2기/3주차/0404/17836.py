from collections import deque

N, M, T = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
visited = [[[False, False]
            for _ in range(M)] for _ in range(N)]  # 수정: 칼의 유무에 따른 방문 상태 관리

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q = deque([(0, 0, 0, False)])  # 시작 위치, 이동 횟수, 칼 보유 여부
    visited[0][0][0] = True  # 칼 없이 방문한 상태 표시

    while q:
        x, y, cnt, has_sword = q.popleft()

        if x == N-1 and y == M-1:
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if has_sword:  # 칼을 가지고 있으면 벽을 무시하고 이동 가능
                    if not visited[nx][ny][1]:  # 칼을 가지고 방문하지 않은 상태
                        visited[nx][ny][1] = True
                        q.append((nx, ny, cnt+1, True))
                else:  # 칼이 없는 경우
                    if data[nx][ny] != 1 and not visited[nx][ny][0]:  # 벽이 아니고, 칼 없이 방문하지 않은 상태
                        visited[nx][ny][0] = True
                        new_has_sword = data[nx][ny] == 2  # 칼을 주운 경우
                        q.append((nx, ny, cnt+1, new_has_sword))
    return float('inf')


result = bfs()
if result <= T:
    print(result)
else:
    print("Fail")
