a, b = map(int, input().split())
total = 0
count = 1
for i in range(1, b+1):
    for _ in range(i):
        if a <= count and count <= b:
            total += i
        count += 1
        if count > b:
            break
print(total)