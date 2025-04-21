def isPrime(num):
    if num < 2:
        return 0
    for i in range(2, int(num**(1/2))+1):
        if num%i == 0:
            return 0
    return 1

m = int(input())
n = int(input())

prime_list = []

for i in range(m, n+1):
    if isPrime(i):
        prime_list.append(i)
    
if len(prime_list) == 0:
    print(-1)
else:
    print(sum(prime_list))
    print(min(prime_list))