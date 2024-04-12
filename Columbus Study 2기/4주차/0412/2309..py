from itertools import combinations
data = [int(input()) for _ in range(9)]
result = []
for seven in combinations(data, 7):
    if sum(seven) == 100:
        result = list(seven)
        break
result.sort()

for i in result:
    print(i)
