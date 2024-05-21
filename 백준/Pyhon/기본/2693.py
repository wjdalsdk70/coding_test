T = int(input())

for _ in range(T):
    data = list(map(int, input().split()))
    data.sort(reverse=True)
    print(data[2])
