# fee = list(map(int, input().split()))
# data = []
# result = 0
# for i in range(3):
#     data.append(list(map(int, input().split())))

# data.sort(key=lambda x: x[0])
# start = data[0][0]
# data.sort(key=lambda x: x[1])
# end = data[-1][1]
# print(data, start, end, fee)

# for i in range(start, end+1):
#     count = 0
#     for d in data:
#         if d[0] <= i and i <= d[1]:
#             count += 1
#     print(count*fee[count-1])
#     result += count*fee[count-1]

# print(result)

a, b, c = map(int, input().split())
result = 0
car = []
point = [0]*101

for _ in range(3):
    start, end = map(int, input().split())
    for j in range(start, end):
        point[j] += 1

for i in point:
    if i == 1:
        result += a
    elif i == 2:
        result += 2*b
    elif i == 3:
        result += 3*c

print(result)
