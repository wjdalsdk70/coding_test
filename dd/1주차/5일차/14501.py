# https://www.acmicpc.net/problem/14501
# 문제 설명: 상담원이 퇴사하기 전까지 최대한 많은 이익을 얻으려고 할 때, 얻을 수 있는 최대 이익을 계산합니다.
# 핵심 개념: 동적 프로그래밍을 사용하여 각 날짜별 최대 이익을 계산합니다.
# 시간 복잡도: O(N^2), 여기서 N은 입력으로 주어진 상담 일수입니다.

n = int(input())  # 상담 가능한 총 일수
data = [list(map(int, input().split())) for _ in range(n)]  # 각 상담의 기간과 이익
dp = [0] * (n+1)  # 각 날짜별 최대 이익을 저장할 DP 테이블

# 모든 상담에 대해 반복
for i in range(n):
    if i + data[i][0] <= n:  # 상담이 퇴사일을 넘지 않는 경우에만 고려
        for j in range(i + data[i][0], n + 1):
            # 상담을 했을 때의 이익이 기존의 최대 이익보다 크면 업데이트
            dp[j] = max(dp[j], dp[i] + data[i][1])

print(dp[-1])  # 마지막 날짜의 최대 이익 출력
