def calc_bracket_value(s):
    stack = []
    temp = 1
    result = 0
    prev = ''
    
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(ch)
            temp *= 2
        elif ch == '[':
            stack.append(ch)
            temp *= 3
        elif ch == ')':
            if not stack or stack[-1] != '(':
                return 0
            if s[i-1] == '(':  # 바로 전이 '('이면 곱한 값을 더해줌
                result += temp
            stack.pop()
            temp //= 2
        elif ch == ']':
            if not stack or stack[-1] != '[':
                return 0
            if s[i-1] == '[':  # 바로 전이 '['이면 곱한 값을 더해줌
                result += temp
            stack.pop()
            temp //= 3
        else:
            return 0  # 예외 처리 (입력값이 이상할 경우)
    
    if stack:  # 아직 남아 있다면 올바른 괄호열이 아님
        return 0
    
    return result

# 입력
s = input().strip()
print(calc_bracket_value(s))