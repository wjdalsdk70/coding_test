# 문제
# 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

s = int(input())
n = 1
sum = 0

while True:
    sum += n
    if sum > s:
        n -= 1
        break
    n += 1

print(n)
