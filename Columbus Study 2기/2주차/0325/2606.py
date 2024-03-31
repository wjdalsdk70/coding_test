# BFS
# from collections import deque
# n = int(input())
# k = int(input())
# edges = [[] for _ in range(n+1)]
# visited = [0 for _ in range(n+1)]

# for _ in range(k):
#     a, b = map(int, input().split())
#     edges[a].append(b)

# q = deque([1])

# while q:
#     node = q.pop()
#     if visited[node] == 0:
#         visited[node] = 1
#     for i in edges[node]:
#         q.appendleft(i)

# print(visited.count(1)-1)

# DFS
n = int(input())
k = int(input())
edges = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(k):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)


def dfs(i):
    visited[i] = True
    for edge in edges[i]:
        if not visited[edge]:
            dfs(edge)


dfs(1)

print(visited.count(True)-1)

# 처음엔 result = [] 로 방문 한 노드를 추가 해줬는데
# visited로 미리 선언하여 방문한 노드를 체크하는 식으로 바꿨다.
