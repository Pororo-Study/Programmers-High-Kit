def solution(sizes):
    w = []
    h = []
    
    for x, y in sizes:
        if x >= y:
            w.append(x)
            h.append(y)
        else:
            h.append(x)
            w.append(y)
    return max(w) * max(h)