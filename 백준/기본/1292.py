start, end = map(int, input().split())
data = []
for i in range(1, end+1):
    for _ in range(i):
        data.append(i)
print(sum(data[start-1:end]))
