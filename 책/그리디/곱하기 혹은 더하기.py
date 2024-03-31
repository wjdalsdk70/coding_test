data = input()

result = int(data[0])

for i in range(1, len(data)):

    num = int(data[i])
    gob = result * num
    if gob <= max(result, num):
        result += num
        continue
    result = gob

print(result)
