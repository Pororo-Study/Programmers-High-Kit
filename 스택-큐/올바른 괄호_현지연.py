# 풀이 1
def solution(s):
    count = 0   # pair count 
    
    for c in s:
        if c == '(':    # '('인 경우 1 더하기
            count += 1
        else:           # ')'인 경우 1 빼기
            count -= 1
        if count < 0:   # 음수가 된다면 올바르지 않은 괄호
            return False
        
    if count != 0:      # 최종 count가 음수가 0이 아니라면 올바르지 않은 괄호
        return False

    return True

# 풀이 2
def solution(s):
    stack = []
    
    for c in s:
        if c == '(':                # '('인 경우 stack에 쌓기
            stack.append('(')
        else:
            if len(stack) == 0:     # ')'이면서 stack이 비어있는 경우
                return False
            elif stack[-1] == '(':  # ')'이면서 stack 맨 위에 '('가 있는 경우
                stack.pop()

    # 마지막에 괄호가 남아있으면 올바르지 않은 괄호
    return False if len(stack) != 0 else True