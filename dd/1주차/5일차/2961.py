# https://www.acmicpc.net/problem/2961
# 문제 설명: 주어진 식재료들로 만들 수 있는 음식 중에서 신맛과 쓴맛의 차이가 가장 작은 음식을 찾아, 그 차이를 출력합니다.
# 핵심 개념: 모든 식재료의 조합을 고려하여 최적의 신맛과 쓴맛의 조화를 찾습니다.
# 시간 복잡도: O(2^n * n), 여기서 n은 식재료의 수입니다. 모든 식재료의 조합을 생성하고 각 조합에 대해 계산을 수행합니다.

from itertools import combinations

result = 1e9  # 최소값을 저장할 변수, 초기값은 충분히 큰 수로 설정
n = int(input())  # 식재료의 수
data = []  # 각 식재료의 신맛과 쓴맛을 저장할 리스트

# 식재료의 신맛과 쓴맛 입력 받기
for _ in range(n):
    data.append(list(map(int, input().split())))

# 1개 이상의 식재료를 사용하는 모든 조합을 고려
for i in range(1, n+1):
    for cook in combinations(data, i):
        S, B = 1, 0  # 신맛은 곱하기, 쓴맛은 더하기로 계산
        for s, b in cook:
            S *= s
            B += b
        result = min(abs(S-B), result)  # 최소 차이 갱신

print(result)  # 결과 출력
