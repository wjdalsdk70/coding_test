n = int(input())
data = list(map(int, input().split()))
data.sort()
print(data.pop() + sum(data)/2)
