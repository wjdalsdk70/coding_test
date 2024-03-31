n = int(input())
data = []

for i in range(n):
    data.append(list(map(int, input().split())))

data.sort(key=lambda x: (x[1], x[0]))
count = 0

while True:
    if len(data) == 0:
        break
    x = 0
    for i in data:
        if i[0] >= x:
            x = i[1]
            data.pop(0)
    count += 1

print(count)
