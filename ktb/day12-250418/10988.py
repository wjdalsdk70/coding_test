data = input()
n = len(data)
jd = True
if n % 2 == 0:
    for i in range(n):
        if data[i] != data[n-i-1]:
            jd = False
            break
else:
    for i in range(n-1):
        if data[i] != data[n-i-1]:
            jd = False
            break

if jd:
    print(1)
else:
    print(0)
