# 수학
# n이 1인 경우를 고려 못함
# n = int(input())
# count = 0

# while (n):
#     if n == 1:
#         count += 1
#         n -= 1
#         continue
#     start = int(n/2)
#     for i in range(start, 0, -1):
#         if i**2 <= n:
#             print(i)
#             count += 1
#             n -= i**2
#             break

# print(count)
# 최소를 찾지 못함

# https://www.acmicpc.net/problem/17626
# 문제 설명: 주어진 자연수 n을 최대 네 개의 제곱수의 합으로 표현할 때 필요한 제곱수의 최소 개수를 찾습니다.
# 핵심 개념: 동적 프로그래밍 또는 브루트포스 접근 방식을 사용하여 문제를 해결합니다. 여기서는 간단한 브루트포스 방식을 사용하되, 효율성을 고려하여 조기 종료 조건을 포함합니다.
# 시간 복잡도: 최악의 경우 O(sqrt(n)^3), n이 매우 클 때 비효율적일 수 있지만, 주어진 문제의 범위 내에서는 충분히 효율적으로 작동합니다.

n = int(input())  # 사용자로부터 자연수 n 입력
arr = [0 if i**0.5 % 1 else 1 for i in range(n+1)]  # 제곱수는 1로, 아니면 0으로 초기화

min_ = 4  # 필요한 제곱수의 최소 개수, 최대값은 4로 시작
for i in range(int(n**0.5), 0, -1):  # n의 제곱근부터 1까지 반복
    if arr[n]:  # n이 제곱수인 경우
        min_ = 1
        break
    elif arr[n-i**2]:  # n에서 i의 제곱을 뺀 값이 제곱수인 경우
        min_ = 2
        break
    else:
        for j in range(int((n-i**2)**0.5), 0, -1):
            if arr[(n-i**2)-j**2]:  # n에서 i의 제곱을 뺀 값에서 j의 제곱을 또 뺀 값이 제곱수인 경우
                min_ = 3
print(min_)  # 결과 출력
