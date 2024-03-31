data = input()

result = []
count = 0

for i in range(len(data)):
    if data[i] == '.':
        if count % 2 != 0:
            count = -1
            break

        result.append(count//4 * 'AAAA')
        result.append((count % 4)//2 * 'BB')
        result.append('.')
        count = 0
    else:
        count += 1

if count % 2 == 0:
    result.append(count//4 * 'AAAA')
    result.append((count % 4)//2 * 'BB')
    print(''.join(result))
else:
    print(-1)

board = input()

board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

if 'X' in board:
    print(-1)

else:
    print(board)
