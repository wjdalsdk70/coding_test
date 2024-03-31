# https://www.acmicpc.net/problem/15721
# 문제 설명: 번데기 게임에서 주어진 순서(t)와 신호(signal)에 해당하는 참가자의 번호를 찾는 문제.
# 핵심 개념: 시뮬레이션, 순서와 규칙에 따른 반복 증가.
# 게임 규칙: "번", "데기"를 시작으로, 게임이 진행될수록 "번", "데기"의 반복 횟수가 2 → 3 → 4 → ... 순으로 증가합니다.
# 시간 복잡도: 게임의 반복 횟수에 비례하는 O(N), N은 입력으로 주어진 순서(t)에 도달하기까지 필요한 총 게임의 수입니다.

a = int(input())  # 참가자 수
t = int(input())  # 찾고자 하는 순서
signal = int(input())  # 찾고자 하는 신호(0은 "번", 1은 "데기")
game = []  # 게임 진행 상황을 저장하는 리스트
b_count = 0  # "번" 카운트
d_count = 0  # "데기" 카운트
n = 1  # 현재 라운드에서 "번"과 "데기"가 추가되는 횟수

while True:
    # 기본 "번", "데기" 추가
    for _ in range(2):
        b_count += 1
        game.append((b_count, 0))  # "번" 추가
        d_count += 1
        game.append((d_count, 1))  # "데기" 추가

    # 라운드별 증가하는 "번", "데기" 추가
    for _ in range(n+1):
        b_count += 1
        game.append((b_count, 0))  # "번" 추가
    for _ in range(n+1):
        d_count += 1
        game.append((d_count, 1))  # "데기" 추가

    # 주어진 순서에 도달했는지 검사
    if b_count >= t or d_count >= t:
        print(game.index((t, signal)) % a)
        break

    n += 1  # 다음 라운드 준비
