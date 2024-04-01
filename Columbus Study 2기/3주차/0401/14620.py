from itertools import combinations

n = int(input())
value = []
data = []
for _ in range(n):
    value.append(list(map(int, input().split())))

for i in range(1, n-1):
    for j in range(1, n-1):
        data.append((i, j))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


min_value = 1000000

for seeds in combinations(data, 3):
    check_list = []
    for x, y in seeds:
        check_list.append((x, y))
        for i in range(4):
            check_list.append((x+dx[i], y+dy[i]))

    if len(check_list) == len(set(check_list)):
        sum = 0
        for x, y in check_list:
            sum += value[x][y]
        min_value = min(min_value, sum)

print(min_value)
