from collections import deque
# N = int(input())
# data = [0] + [int(input()) for _ in range(N)]


# def bfs(n):
#     q = deque([(data[n])])
#     visited[n] = True
#     result = []
#     while q:
#         x = q.popleft()
#         if not visited[data[x]]:
#             visited[data[x]] = True
#             result.append(x)
#             q.append(data[x])
#     return result


# max_result = []
# self_list = []

# for i in range(1, N+1):
#     visited = [False]*(N+1)
#     r_list = bfs(i)
#     if len(max_result) < len(r_list):
#         max_result = r_list
#     if i == data[i]:
#         self_list.append(i)

# max_result = max_result+self_list
# max_result.sort()
# print(len(max_result))
# for m in max_result:
#     print(m)

N = int(input())
data = [0] + [int(input()) for _ in range(N)]


def bfs(start):
    q = deque([start])
    visited[start] = True
    result = [start]
    while q:
        current = q.popleft()
        next_node = data[current]
        if not visited[next_node]:
            visited[next_node] = True
            result.append(next_node)
            q.append(next_node)
        elif next_node == start:  # 순환을 찾음
            return result
    return []  # 순환을 찾지 못함


max_result = []
self_list = []
visited = [False] * (N + 1)

for i in range(1, N + 1):
    if not visited[i]:
        result = bfs(i)
        if len(result) > len(max_result):
            max_result = result
    if i == data[i]:
        self_list.append(i)

# 출력
print(len(max_result))
for m in max_result:
    print(m)
