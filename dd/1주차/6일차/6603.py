# https://www.acmicpc.net/problem/6603
# 문제 설명: 로또 번호를 고르는 문제입니다. 1부터 49까지의 숫자 중 주어진 숫자들로 만들 수 있는 모든 가능한 6개 숫자의 조합을 출력합니다.
# 핵심 개념: 조합을 사용하여 주어진 숫자들로부터 가능한 모든 6개 숫자의 조합을 생성합니다.

from itertools import combinations

while True:
    # 사용자 입력 받기. 첫 번째 숫자는 숫자들의 개수이며, 그 뒤로 해당 숫자들이 주어집니다.
    d = list(map(int, input().split()))
    if d[0] == 0:  # 입력의 끝을 나타내는 0이면 반복 종료
        break

    # 입력받은 번호로부터 6개를 선택하는 모든 조합 생성 및 출력
    for c in combinations(d[1:], 6):  # d[1:]로 첫 번째 숫자(숫자들의 개수)를 제외한 숫자들만을 사용해 조합을 생성
        print(' '.join(map(str, c)))  # 생성된 조합을 공백으로 구분하여 출력
    print()  # 입력 케이스 사이에 빈 줄 출력
