# BFS => 메모리 초과
# from collections import deque
# N = int(input())


# def bfs():
#     q = deque([(i, N) for i in range(1, 10)])
#     count = 0

#     while q:
#         num, w = q.popleft()
#         if w == 1:
#             count += 1
#             continue
#         if num+1 != 10:
#             q.append((num+1, w-1))
#         if num-1 != -1:
#             q.append((num-1, w-1))

#     return count


# print(bfs())

# DP 풀이법
N = int(input())
dp = [[0 for _ in range(10)] for _ in range(N+1)]

# 초기값 설정
for i in range(1, 10):
    dp[1][i] = 1

# 점화식을 이용하여 DP 테이블 채우기
for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

# 답 구하기
answer = sum(dp[N]) % 1000000000
print(answer)
