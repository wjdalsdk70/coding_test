# https://www.acmicpc.net/problem/5568
# 문제 설명: n장의 카드 중 k장을 골라 이어 붙여 만들 수 있는 서로 다른 수의 개수를 구합니다.
# 핵심 개념: 순열(permutations)을 사용하여 가능한 모든 카드 조합의 순서를 고려합니다.
# 시간 복잡도: O(nPk * k), 여기서 nPk는 n개 중에서 k개를 선택하는 순열의 수이고, k는 문자열로 변환하는 데 걸리는 시간입니다.

from itertools import permutations

n = int(input())  # 카드의 총 수
k = int(input())  # 선택할 카드의 수
cards = [input() for _ in range(n)]  # 카드 입력
result = set()  # 중복을 허용하지 않는 집합을 사용해 결과 저장

for card in permutations(cards, k):  # 가능한 모든 순열 생성
    result.add(''.join(card))  # 생성된 순열을 문자열로 변환하여 집합에 추가

print(len(result))  # 고유한 수의 개수 출력
