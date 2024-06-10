def bean(n, p):
    if n == 1:
        return "Rr"
    
    parent = bean(n - 1, (p - 1) // 4 + 1)
    if parent == "RR" or parent == "rr":
        return parent
    
    if p % 4 == 0:
        return "rr"
    elif p % 4 == 1:
        return "RR"
    else:
        return "Rr"
    
def solution(queries):
    answer = []
    for n, p in queries:
        answer.append(bean(n, p))
    return answer
