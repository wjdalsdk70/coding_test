T = int(input())
for _ in range(T):
    n = int(input())
    bin_n = bin(n)
    nlt = list(map(int, str(bin_n)[:1:-1]))
    indices = [index for index, value in enumerate(nlt) if value == 1]
    print(*indices)
