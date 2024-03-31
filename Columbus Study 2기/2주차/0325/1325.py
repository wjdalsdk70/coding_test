from collections import deque

n, m = map(int, input().split())
edges = [[] for _ in range(n+1)]
count = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    edges[b].append(a)


def bfs(i):
    d = deque([i])
    visit = [False] * (n+1)
    visit[i] = True
    cnt = 1
    while d:
        i = d.popleft()
        for j in edges[i]:
            if not visit[j]:
                d.append(j)
                visit[j] = True
                cnt += 1
    return cnt


for i in range(1, n+1):
    count[i] = bfs(i)

max_value = max(count)
max_elements = [i for i in range(1, n+1) if count[i] == max_value]
print(' '.join(list(map(str, max_elements))))

# def dfs(i):
#     visited[i] = True
#     total = 0
#     for edge in edges[i]:
#         if not visited[edge]:
#             total += 1 + dfs(edge)
#     count[i] = total
#     return total


# for v in range(1, n+1):
#     visited = [False] * (n+1)
#     count = [0] * (n+1)
#     result[v] = dfs(v)
# max_value = max(count)
# max_elements = [i for i in range(1, n+1) if count[i] == max_value]
# print(' '.join(list(map(str, max_elements))))

# 사이클이 생기는 경우 고려 못함
