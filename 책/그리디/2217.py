N = int(input())
data = []
for i in range(N):
    m = int(input())
    data.append(m)

data.sort()
l = len(data)

for i in range(l):
    data[i] *= (l-i)

print(max(data))
