import sys
from collections import deque
N = int(sys.stdin.readline())
data = deque([])

for _ in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        data.append(cmd[1])
    elif cmd[0] == "pop":
        if len(data) == 0:
            print(-1)
        else:
            print(data.popleft())
    elif cmd[0] == "size":
        print(len(data))
    elif cmd[0] == "empty":
        if len(data) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == "front":
        if len(data) == 0:
            print(-1)
        else:
            print(data[0])
    elif cmd[0] == "back":
        if len(data) == 0:
            print(-1)
        else:
            print(data[-1])
