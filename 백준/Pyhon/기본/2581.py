M = int(input())
N = int(input())


def solution(num):
    jd = True
    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            jd = False
            break
    return jd


result = []
for i in range(M, N+1):
    if (solution(i)):
        result.append(i)
if len(result) > 0:
    print(sum(result))
    print(min(result))
else:
    print(-1)
