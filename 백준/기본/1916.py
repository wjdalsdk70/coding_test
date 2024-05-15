N = int(input())
M = int(input())
bus = []
cost = [[0]*N for _ in range(N+1)]
result = [0]*(N+1)
for _ in range(M):
    a, b, c = map(int, input().split())
    cost[a][b] = c
start, end = map(int, input().split())
