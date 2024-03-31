# https://www.acmicpc.net/problem/2798
# 문제 설명: 주어진 카드 중 3장을 골라, 주어진 M을 넘지 않으면서 M에 최대한 가까운 카드 합을 찾는 문제.
# 핵심 개념: 조합을 사용한 브루트 포스 알고리즘.
# 브루트 포스 사용 조건: 가능한 모든 조합을 검사해야 할 때 사용. 이 문제에서는 주어진 카드들 중 3장의 조합을 모두 고려합니다.
# 시간 복잡도: O(C(n, 3)), 여기서 n은 주어진 카드의 수이며 C(n, 3)은 n개 중 3개를 고르는 조합의 수를 의미합니다.

from itertools import combinations

n, m = map(int, input().split())  # n은 카드의 수, m은 블랙잭 목표 합
data = list(map(int, input().split()))  # 카드에 적힌 수들

result = 0  # 결과값 초기화

# 가능한 모든 카드 3장 조합에 대해 반복
for cards in combinations(data, 3):
    s = sum(cards)  # 선택된 카드 3장의 합
    # 이전에 찾은 결과보다 크고 m을 넘지 않는 경우, 결과 갱신
    if result < s <= m:
        result = s

print(result)  # 결과 출력
