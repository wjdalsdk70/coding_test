from collections import Counter
data = [int(input()) for _ in range(10)]
var = Counter(data).most_common()
print(sum(data)//10)
print(var[0][0])
