import sys
import heapq as hq

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x:
        hq.heappush(heap, (-x, x))
    else:
        if len(heap) > 0:
            print(hq.heappop(heap)[1])
        else:
            print(0)
