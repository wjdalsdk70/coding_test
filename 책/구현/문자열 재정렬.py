data = input()
char_list = []
sum = 0

for i in data:
    if i.isalpha():
        char_list.append(i)
    else:
        sum += int(i)

char_list.sort()

if sum != 0:
    char_list.append(str(sum))
print(''.join(char_list))
