def solution(s):
    c = 0
    for i in s:
        if c==0 and i==')':
            return False
        elif i == ')':
            c -= 1
        else:
            c += 1
    return not c