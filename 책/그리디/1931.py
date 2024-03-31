n = int(input())
data = []

for i in range(n):
    data.append(list(map(int, input().split())))

data.sort(key=lambda x: (x[1], x[0]))

x = 0
result = []

for i in data:
    if i[0] >= x:
        result.append(i)
        x = i[1]

print(len(result))
