def solution(s):
    stack = []
    for tmp in s:
        if tmp == '(':
            stack.append(tmp)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True