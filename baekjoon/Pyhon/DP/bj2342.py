INF = 10**9

def build_cost():
    cost = [[0] * 5 for _ in range(5)]
    opp = {(1,3), (2,4), (3,1), (4,2)}
    for i in range(5):
        for j in range(5):
            if i == j:
                cost[i][j] = 1 if i != 0 else 1
            elif i == 0 or j == 0:
                cost[i][j] = 2
            elif (i,j) in opp:
                cost[i][j] = 4
            else:
                cost[i][j] = 3
    return cost

def solution():
    steps = list(map(int, input().split()))
    if not steps:
        print(0); return
    if steps[-1] == 0:
        steps.pop()
        
    cost = build_cost()
    
    dp = [[INF]*5 for _ in range(5)]
    dp[0][0] = 0
    
    for x in steps:
        next_dp = [[INF]*5 for _ in range(5)]
        for l in range(5):
            row = dp[l]
            for r in range(5):
                cur = row[r]
                if cur == INF:
                    continue
                if x != r:
                    c = cur + cost[l][x]
                    if c < next_dp[x][r]:
                        next_dp[x][r] = c
                if x != l:
                    c = cur + cost[l][x]
                    if c < next_dp[x][r]:
                        next_dp[l][x] = c
        dp = next_dp
    ans = min(min(row) for row in dp)
    print(ans)
            
if __name__ == "__main__":
    solution()