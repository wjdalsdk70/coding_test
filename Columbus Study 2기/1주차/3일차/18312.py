# https://www.acmicpc.net/problem/18312
# 문제 설명: 00:00:00부터 N:59:59까지의 모든 시간 중에서 특정 숫자 K가 하나라도 포함되는 모든 시간의 경우의 수를 찾아내는 문제.
# 핵심 개념: 브루트 포스 알고리즘을 통한 모든 가능한 시간의 조합 탐색.
# 시간 복잡도: O(N * 60 * 60), 여기서 N은 주어진 최대 시간입니다. 모든 시간, 분, 초에 대해 반복문을 실행합니다.

n, k = map(int, input().split())  # n은 최대 시간, k는 찾고자 하는 숫자
count = 0  # 조건을 만족하는 시간의 개수


def num2time(a):
    # 숫자를 시간 형태의 문자열로 변환하는 함수. 한 자릿수일 경우 앞에 '0'을 붙임
    return str(a) if len(str(a)) != 1 else '0'+str(a)


# 모든 시간에 대해 반복
for i in range(n+1):
    for j in range(60):
        for l in range(60):
            # 시, 분, 초를 문자열로 합침
            time = num2time(i) + num2time(j) + num2time(l)
            # 합친 문자열에 k가 포함되어 있는지 확인
            if str(k) in time:
                count += 1  # 포함되어 있으면 카운트 증가

print(count)  # 결과 출력
