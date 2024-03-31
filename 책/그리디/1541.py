data = input()
s = []
result = 0
if data.find('-') != -1:
    m_index = data.find('-')
    result += sum(list(map(int, data[:m_index].split('+'))))
    data = data.replace('-', '+')
    result -= sum(list(map(int, data[m_index+1:].split('+'))))
else:
    result = sum(list(map(int, data.split('+'))))

print(result)

arr = input().split('-')

s = 0

for i in arr[0].split('+'):
    s += int(i)

for i in arr[1:]:
    for j in i.split('+'):
        s -= int(j)
print(s)
