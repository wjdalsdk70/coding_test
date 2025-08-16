data = [map(int, input().split()) for _ in range(10)]
result = []
ct = 0
for ot, it in data:
    ct = ct - ot + it
    result.append(ct)
print(max(result))
