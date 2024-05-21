# S = input()
# P = input()
# jd = False
# for i in range(len(S)):
#     count = 0
#     if S[i] == P[0] and i+len(P)-1 < len(S):
#         for j in range(len(P)):
#             if S[i+j] == P[j]:
#                 count += 1
#     if count == len(P):
#         jd = True
#         break
# if jd:
#     print(1)
# else:
#     print(0)
from sys import stdin
S = stdin.readline().rstrip()
P = stdin.readline().rstrip()
if P in S:
    print(1)
else:
    print(0)
