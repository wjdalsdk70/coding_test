H, W = map(int, input().split())
walls = list(map(int, input().split()))
worlds = [[0] * W for _ in range(H)]

for i in range(W):
    for j in range(H-walls[i],H):
        worlds[j][i] = 1

for i in range(H):
    for j in range(W):
        if worlds[i][j] == 0 and 0 < j and j < W-1:
            if 
