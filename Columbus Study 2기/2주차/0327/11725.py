from collections import deque

n = int(input())
eg = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    eg[a].append(b)
    eg[b].append(a)


def bfs():
    q = deque([1])

    while (q):
        node = q.popleft()
        for e in eg[node]:
            parent[e] = node
            eg[e].remove(node)
            q.append(e)


bfs()
print(*parent[2:])
