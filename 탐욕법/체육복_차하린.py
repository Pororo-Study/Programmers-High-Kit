def solution(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    
    for x in set_reserve:
        if x-1 in set_lost:
            set_lost.remove(x-1)
        elif x+1 in set_lost:
            set_lost.remove(x+1)
    return n-len(set_lost)