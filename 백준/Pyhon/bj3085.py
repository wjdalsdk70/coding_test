def check(arr):
    n = len(arr)
    answer = 1

    # 행 체크
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            answer = max(answer, cnt)

    # 열 체크
    for j in range(n):
        cnt = 1
        for i in range(1, n):
            if arr[i][j] == arr[i-1][j]:
                cnt += 1
            else:
                cnt = 1
            answer = max(answer, cnt)

    return answer


n = int(input())
arr = [list(input()) for _ in range(n)]
answer = 0

# 가로로 인접한 두 사탕 교환
for i in range(n):
    for j in range(n-1):
        # 인접한 두 사탕 교환
        arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

        # 최대 사탕 개수 체크
        temp = check(arr)
        answer = max(answer, temp)

        # 원위치
        arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

# 세로로 인접한 두 사탕 교환
for i in range(n-1):
    for j in range(n):
        # 인접한 두 사탕 교환
        arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

        # 최대 사탕 개수 체크
        temp = check(arr)
        answer = max(answer, temp)

        # 원위치
        arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

print(answer)
