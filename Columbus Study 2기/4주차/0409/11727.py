n = int(input())

tile = [-1]*1001
tile[1] = 1
tile[2] = 3

for i in range(3, n+1):
    tile[i] = tile[i-2] * 2 + tile[i-1]


print(tile[n] % 10007)
