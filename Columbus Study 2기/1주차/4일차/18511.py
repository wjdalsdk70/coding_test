# https://www.acmicpc.net/problem/18511
# 문제 설명: 주어진 자연수 N 이하에서, 주어진 자연수 집합 K의 원소만을 사용해 만들 수 있는 가장 큰 수를 찾습니다.
# 핵심 개념: 중복 순열을 이용한 브루트포스 방식으로 가능한 모든 수를 생성하고 검사합니다.
# 시간 복잡도: O(k^n), 여기서 k는 집합 K의 원소의 수, n은 생성할 수의 최대 자릿수입니다.

from itertools import product

n, k = map(int, input().split())  # 사용자로부터 N과 K의 크기 입력
data = list(map(int, input().split()))  # K 집합의 원소 입력
result = 0  # 결과 초기화

# N의 자릿수부터 1자리까지 가능한 모든 수 생성
for j in range(len(str(n)), 0, -1):
    # 집합 K의 원소로 구성된 중복 순열 생성
    for i in product(data, repeat=j):
        # 생성된 중복 순열을 정수로 변환
        res = int(''.join(map(str, i)))
        # 생성된 수가 N 이하이고 현재까지의 결과보다 크면 결과 갱신
        if res <= n and res > result:
            result = res
    # 가능한 결과를 찾은 경우 반복 종료
    if result != 0:
        break

print(result)  # 결과 출력
