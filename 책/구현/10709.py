h, w = map(int, input().split())

result = ''

for _ in range(h):
    data = input()
    count = -1
    for d in data:
        if d == 'c':
            result += '0 '
            count = 0
        else:
            if count == -1:
                result += '-1 '
            else:
                count += 1
                result += str(count) + ' '
    result += '\n'
print(result)
