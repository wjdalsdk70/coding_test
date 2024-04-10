n, k = list(map(int, input().split()))
s = [0] + list(map(int, input().split()))
dp = [[0]*(k+1) for _ in range(n+1)]  # [처음부터i까지][삭제횟수]
for i in range(1, n+1):
    for k in range(k+1):
        # 짝수인 경우
        if s[i] % 2 == 0:
            # 삭제횟수는 안 늘어남, 수열길이는 늘어남
            # 이전 수열 까지의 길이 + 1
            dp[i][k] = dp[i-1][k] + 1
        # 홀수인경우 k = 0 일 경우삭제 작업을 아직 한 번도 수행하지 않았다는 뜻 홀수인수를 삭제해도 현재까지의 연속 부분 수열에는 영향을 주지 않는다,
        if k != 0 and s[i] % 2:
            # 이전 상태에서 k-1번의 삭제 횟수를 사용한 경우의 값 >> s[i]를 삭제를 했다는 뜻
            dp[i][k] = dp[i-1][k-1]
res = []
for i in dp:
    res.append(i[k])
print(max(res))
