memo = {}
memo[1] = 1


def fac(i):
    if i == 0:
        return 1

    memo[i] = i * fac(i-1)
    return memo[i]


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    # data = [i for i in range(M)]
    # print(fac(M))
    # print(fac(N))
    print(int(fac(M)/(fac(N)*fac(M-N))))
