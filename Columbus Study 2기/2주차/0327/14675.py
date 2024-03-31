from collections import deque
n = int(input())
edges = []
eg = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    edges.append((a, b))
    eg[a].append(b)
    eg[b].append(a)


# def bfs(l):
#     l = deque(l)
#     cnt = 0
#     while (l):
#         node = l.popleft()
#         for e in eg[node]:
#             l.append(e)
#             cnt += 1
#     if
#     return cnt


q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    b = False
    if t == 1:
        b = False
        if len(eg[k]) >= 2:
            b = True
        # for e in eg[k]:
            # bfs(e)
    if t == 2:
        b = True
    if b:
        print("yes")
    else:
        print("no")
