def check(board, n):
    max_candies = 1

    # 행 기준 체크
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if board[i][j] == board[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            max_candies = max(max_candies, cnt)

    # 열 기준 체크
    for j in range(n):
        cnt = 1
        for i in range(1, n):
            if board[i][j] == board[i - 1][j]:
                cnt += 1
            else:
                cnt = 1
            max_candies = max(max_candies, cnt)

    return max_candies

def solve(board, n):
    max_candies = 0

    for i in range(n):
        for j in range(n):
            # 오른쪽과 교환
            if j + 1 < n:
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
                max_candies = max(max_candies, check(board, n))
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]  # 복원

            # 아래쪽과 교환
            if i + 1 < n:
                board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
                max_candies = max(max_candies, check(board, n))
                board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]  # 복원

    return max_candies

# 입력
n = int(input())
board = [list(input().strip()) for _ in range(n)]

# 출력
print(solve(board, n))