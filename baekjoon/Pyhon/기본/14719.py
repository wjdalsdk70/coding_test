H, W = map(int, input().split())
data = list(map(int, input().split()))
world = [[0] * W for _ in range(H)]
count = 0
for i in range(W):
    for j in range(H-data[i], H):
        world[j][i] = 1

for i in range(H):
    for j in range(W):
        if world[i][j] == 0 and 0 < j and j < W-1:
            if 1 in world[i][:j] and 1 in world[i][j+1:]:
                count += 1
print(count)
