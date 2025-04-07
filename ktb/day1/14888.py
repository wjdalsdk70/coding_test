# 백준 14888 - 연산자 끼워넣기
N = int(input())  # 숫자 개수 입력
nums = list(map(int, input().split()))  # 숫자 리스트 입력
op = list(map(int, input().split()))  # 연산자 사용 가능 횟수 입력 (+, -, *, //)
result = []


def dfs(num, index):
    if index == N - 1:
        result.append(num)
        return

    if op[0] > 0:
        op[0] -= 1
        dfs(num + nums[index + 1], index + 1)
        op[0] += 1

    if op[1] > 0:
        op[1] -= 1
        dfs(num - nums[index + 1], index + 1)
        op[1] += 1

    if op[2] > 0:
        op[2] -= 1
        dfs(num * nums[index + 1], index + 1)
        op[2] += 1

    if op[3] > 0:
        op[3] -= 1
        if num < 0:
            dfs(-(-num // nums[index + 1]), index + 1)
        else:
            dfs(num // nums[index + 1], index + 1)
        op[3] += 1


dfs(nums[0], 0)
print(max(result))
print(min(result))
