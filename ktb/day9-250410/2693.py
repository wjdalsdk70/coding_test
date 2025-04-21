t = int(input())
results = []
for _ in range(t):
    arr = list(map(int, input().split()))
    arr.sort()
    results.append(arr[-3])
for result in results:
    print(result)