# from collections import deque
# n, k = map(int, input().split())
# mc = 100000
# count = 0


# def bfs(min_cnt):
#     q = deque([(n, 0)])

#     while (q):
#         x, cnt = q.popleft()
#         if cnt > min_cnt:
#             continue
#         if x == k:
#             min_cnt = cnt
#             count += 1
#         if 0 <= x-1 <= 100000:
#             q.append((x-1, cnt+1))
#         if 0 <= x+1 <= 100000:
#             q.append((x+1, cnt+1))
#         if 0 <= 2*x <= 100000:
#             q.append((2*x, cnt+1))

#     return min_cnt


# print(bfs(mc))
# print(count)
from collections import deque

n, k = map(int, input().split())
visited = [False] * 100001  # 방문 체크를 위한 리스트
count = 0  # 목표 위치에 도달하는 방법의 수
min_cnt = float('inf')  # 최소 이동 횟수


def bfs():
    global count, min_cnt
    q = deque([(n, 0)])
    visited[n] = True

    while q:
        x, cnt = q.popleft()
        visited[x] = True  # 현재 위치 방문 처리
        if x == k:
            if cnt < min_cnt:
                min_cnt = cnt
                count = 1
            elif cnt == min_cnt:
                count += 1
            continue

        # x-1, x+1, 2*x 위치로 이동
        for nx in (x-1, x+1, 2*x):
            if 0 <= nx <= 100000 and not visited[nx]:
                q.append((nx, cnt+1))


bfs()
print(min_cnt)
print(count)
