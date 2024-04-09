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


# => DP 활용
# n = int(input())

# win = [-1]*10001

# win[1] = 1 #SK
# win[2] = 0 #CY
# win[3] = 1 #SK

# for i in range(4,n+1):
#     if win[i-1] == 1 or win[i-3] == 1:
#         win[i] = 0
#     else:
#         win[i] = 1

# if win[n]==1:
#     print('SK')
# else:
#     print('CY')
