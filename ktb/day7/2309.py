arr = []

for _ in range(9):
    arr.append(int(input()))

total = sum(arr)

for i in range(9):
    for j in range(i+1, 9):
        if total - (arr[i] + arr[j]) == 100:
            excluded = [arr[i], arr[j]]
            result = [x for x in arr if x not in excluded]
            result.sort()
            for a in result:
                print(a)
            exit