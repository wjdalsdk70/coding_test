n, m, t = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 구름이의 집은 (0,0), 탈출구는 (n-1, m-1)
# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(k):
    visited = [[[False] * m for _ in range(n)] for _ in range(t+1)]
    q = [(0, 0, 0, k)]  # x, y, time, 현재 에너지
    visited[0][0][0] = True

    while q:
        x, y, time, energy = q.pop(0)

        # 도착지점 도달 시 성공
        if x == n-1 and y == m-1:
            return True

        # 제한시간 도달 시 실패
        if time == t:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[time+1][nx][ny]:
                # 쑥대밭인 경우 이동 불가
                if graph[nx][ny] == 0:
                    continue

                # 땅에서 땅으로 이동
                if graph[x][y] == 2 and graph[nx][ny] == 2:
                    new_energy = min(k, energy + 1)  # 1초 쉬면서 에너지 1 충전
                    q.append((nx, ny, time+1, new_energy))
                    visited[time+1][nx][ny] = True
                # 날아서 이동 (땅->하늘, 하늘->하늘, 하늘->땅)
                elif energy >= 1:  # 에너지 1이상 필요
                    q.append((nx, ny, time+1, energy-1))
                    visited[time+1][nx][ny] = True
    return False


# 이분탐색으로 최소 K 찾기
left = 1  # 최소 1의 에너지는 필요
right = t  # 최대 K값은 t를 넘을 수 없음

answer = -1
while left <= right:
    mid = (left + right) // 2
    if bfs(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
