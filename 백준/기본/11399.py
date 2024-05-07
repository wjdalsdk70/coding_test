n = int(input())
data = list(map(int, input().split()))

data.sort()
sum = 0
for i in range(len(data)):
    sum += data[i]*(n-i)

print(sum)
