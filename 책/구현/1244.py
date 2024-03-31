n = int(input())
data = list(map(int, input().split()))

num = int(input())


for _ in range(num):
    gender, number = map(int, input().split())
    if gender == 1:
        for i in range(number-1, n, number):
            if data[i] == 1:
                data[i] = 0
            else:
                data[i] = 1
    else:
        for i in range(n-number):
            if data[number-i-1] == data[number+i-1]:
                if i == 0:
                    if data[number-1] == 1:
                        data[number-1] = 0
                    else:
                        data[number-1] = 1
                else:
                    if data[number-1-i] == 1:
                        data[number-1-i] = 0
                        data[number-1+i] = 0
                    else:
                        data[number-1-i] = 1
                        data[number-1+i] = 1
            else:
                break
            if number-i-1 == 0 or number+i-1 == n-1:
                break

print(' '.join(map(str, data)))
