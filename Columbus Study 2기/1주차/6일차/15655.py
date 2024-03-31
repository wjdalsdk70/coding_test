# https://www.acmicpc.net/problem/15655

from itertools import combinations

n, m = map(int, input().split())

data = list(map(int, input().split()))
sort_list = []

for d in combinations(data, m):
    sort_list.append(sorted(d))

sort_list.sort()
for s in sort_list:
    print(' '.join(map(str, s)))
