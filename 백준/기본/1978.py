n = int(input())
nums = list(map(int, input().split()))
count = 0
for num in nums:
    jd = True
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                jd = False
                break
        if jd:
            count += 1
print(count)
