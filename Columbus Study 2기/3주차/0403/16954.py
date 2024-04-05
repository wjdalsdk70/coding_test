from collections import deque
d = [input() for _ in range(8)]

dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]


def move_wall(data):
    # 벽을 한 칸씩 아래로 이동시키는 함수
    new_data = ['........'] + data[:-1]
    return new_data


def bfs(data):
    q = deque([(7, 0, data)])
    visited = set()

    while (q):
        x, y, cur_data = q.popleft()
        next_data = move_wall(cur_data)
        if x == 0 and y == 7:
            return 1
        for i in range(9):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 8 and 0 <= ny < 8 and cur_data[nx][ny] == '.':
                if (nx, ny, ''.join(next_data)) not in visited and next_data[nx][ny] != '#':
                    q.append((nx, ny, next_data))
                    visited.add((nx, ny, ''.join(next_data)))

    return 0


print(bfs(d))
