N, M = map(int, input().split())
data = list(map(int, input().split()))

total = (N * (N-1))/2
sub = 0
data.sort()

for i in set(data):
    j = data.count(i)
    sub += int((j * (j-1))/2)

print(total - sub)
