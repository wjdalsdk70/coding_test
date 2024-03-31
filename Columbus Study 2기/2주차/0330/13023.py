# n, m = map(int, input().split())
# eg = [[] for _ in range(n)]

# for _ in range(m):
#     a, b = map(int, input().split())
#     eg[a].append(b)
#     eg[b].append(a)


# def dfs(i, v, cnt):
#     v[i] = True
#     # print(i, cnt)
#     if cnt == 5:
#         return 1
#     r = 0
#     for e in eg[i]:
#         if not v[e]:
#             r = dfs(e, v.copy(), cnt+1)
#         if r:
#             break
#     return r


# result = 0
# for i in range(0, n):
#     visited = [False]*(n)
#     result = dfs(i, visited, 1)
#     if result:
#         break

# print(result)

# => GPT 활용 / 메모리, 시간 절약
n, m = map(int, input().split())
eg = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    eg[a].append(b)
    eg[b].append(a)


def dfs(i, v, cnt):
    if cnt == 5:
        return 1
    v[i] = True
    result = 0
    for e in eg[i]:
        if not v[e]:
            result = dfs(e, v, cnt+1)
            if result:
                break
    v[i] = False  # 여기에서 노드의 방문 상태를 되돌립니다.
    return result


result = 0
visited = [False]*n  # 방문한 노드를 추적하는 리스트를 한 번만 생성합니다.

for i in range(n):
    if dfs(i, visited, 1):
        result = 1
        break

print(result)
