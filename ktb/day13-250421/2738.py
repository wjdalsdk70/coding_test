n, m = map(int, input().split())
a = [ list(map(int, input().split())) for _ in range(n)]
b = [ list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        a[i][j] += b[i][j]

for row in a:
    print(' '.join(map(str, row)))