# 백준 2501 - 약수 구하기
# a의 약수를 구하고 오름차순으로 b번째 약수를 출력
a, b = map(int, input().split())

result = 0
count = 0

for i in range(1, a+1):
    if a % i == 0 :
        count += 1
    if count == b:
        result = i
        break

if result == 0:
    print(0)     
else: 
    print(result)
