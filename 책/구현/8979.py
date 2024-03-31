n, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

data.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)


print(data[k-1][0])
