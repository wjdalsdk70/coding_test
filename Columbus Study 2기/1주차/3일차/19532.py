# https://www.acmicpc.net/problem/19532
# 문제 설명: 주어진 선형 방정식 시스템 a*x + b*y = c 와 d*x + e*y = f 의 정수 해 x, y를 찾습니다.
# 핵심 개념: 가능한 모든 정수 해를 주어진 범위 내에서 전수 조사하는 브루트포스 방식.
# 이 문제는 대수적 조작을 사용하여 x와 y를 직접 계산하는 것이 더 효율적일 수 있지만, 브루트포스 접근 방식은 간단하며 정의된 검색 공간 내에서 해를 찾는 것을 보장합니다.
# 시간 복잡도: O(n^2), 여기서 n은 각 변수가 취할 수 있는 값의 범위입니다. 이 경우 n = 1999(-999에서 999까지).

a, b, c, d, e, f = map(int, input().split())  # 계수와 상수 입력

# x와 y의 가능한 모든 값에 대해 -999부터 999까지 반복
for x in range(-999, 1000):
    for y in range(-999, 1000):
        # (x, y)가 방정식 시스템의 해인지 확인
        if a*x + b*y == c and d*x + e*y == f:
            print(x, y)  # 해를 출력
            break  # 해를 찾으면 반복 종료
