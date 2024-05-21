import sys
input = sys.stdin.readline

n1, n2 = map(int, input().split())
a, b = n1, n2
while b != 0:
    a, b = b, a % b
gcd = a
lcm = n1*n2//gcd

print(gcd)
print(lcm)
