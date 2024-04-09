N = int(input())
memo = {}
# 홀이면 True 짝이면 False
memo[1] = True
for i in range(2, N+1):
    memo[i] = not memo[i-1]

if memo[N]:
    print("SK")
else:
    print("CY")
