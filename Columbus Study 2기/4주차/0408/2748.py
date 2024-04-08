memo = {}
memo[0] = 0
memo[1] = 1
n = int(input())


# def fibo(i):
#     if i == 0 and i == 1:
#         return 1

#     memo[i] = fibo(i-2)+fibo(i-1)
#     return memo[i]

for i in range(2, n+1):
    memo[i] = memo[i-2] + memo[i-1]

print(memo[n])
