import sys
N, S = map(int, sys.stdin.readline().split())

data = list(map(int, sys.stdin.readline().split()))
start, end = 0, 0
sum = 0
result = sys.maxsize
while (True):
    if sum >= S:
        result = min(result, end-start)
        sum -= data[start]
        start += 1
    elif end == N:
        break
    else:
        sum += data[end]
        end += 1

if result == sys.maxsize:
    print(0)
else:
    print(result)
