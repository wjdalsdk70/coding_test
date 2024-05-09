N = int(input())
adj = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    adj[i].append(int(input()))


def dfs(num):
    if visited[num] == False:
        visited[num] == True
        for a in adj[num]:
            tmp_up.add(num)
            tmp_bottom.add(a)

            if tmp_up == tmp_bottom:
                ans.extend(list(tmp_bottom))
                return

        dfs(a)
    visited[num] = False


ans = []

for i in range(1, N + 1):
    visited = [False] * (N + 1)  # 위에 값 기준으로
    tmp_up = set()
    tmp_bottom = set()

    dfs(i)

ans = list(set(ans))
ans.sort()

print(len(ans))
for a in ans:
    print(a)

# import sys
# input=sys.stdin.readline
# def dfs(v,i):
#     visited[v]=True
#     w=data[v]
#     if not visited[w]:
#         dfs(w,i)
#     elif visited[w] and w==i:
#         result.append(w)
# n=int(input())
# data=[0]+[int(input()) for _ in range(n)]
# result=[]
# for i in range(1,n+1):
#     visited=[False]*(n+1)
#     dfs(i,i)
# print(len(result))
# result.sort()
# for i in result:
#     print(i)
