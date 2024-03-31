data = input()
mid = int(len(data)/2)
result = 0
for i in range(mid):
    result += int(data[i])

for i in range(mid, len(data)):
    result -= int(data[i])

if result == 0:
    print('LUCKY')
else:
    print('READY')
