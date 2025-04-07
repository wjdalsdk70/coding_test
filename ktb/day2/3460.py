# 3460번 - 이진수
import re

T = int(input())
nums = [int(input()) for _ in range(T)]
results = []
for num in nums:
    result = []
    str_num = str(bin(num))
    for text in re.finditer('1', str_num[-1:1:-1]):
        result.append(text.start())
    results.append(result)

for row in results:
    print(*row)