data = input().upper()
word_list = list(set(data))
wtl = []

for i in word_list:
    cnt = data.count(i)
    wtl.append(cnt)

if wtl.count(max(wtl)) > 1:
    print('?')
else:
    print(word_list[wtl.index(max(wtl))])
