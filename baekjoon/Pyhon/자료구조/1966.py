import sys
from collections import deque
N = int(sys.stdin.readline())
for _ in range(N):
    M, prio = map(int, sys.stdin.readline().split())
    data = list(map(int, sys.stdin.readline().split()))
    count = 0
    q = deque(data)

    while (q):
        best = max(q)
        first = q.popleft()
        prio -= 1

        if best == first:
            count += 1
            if prio < 0:
                print(count)
                break
        else:
            q.append(first)
            if prio < 0:
                prio = len(q)-1
