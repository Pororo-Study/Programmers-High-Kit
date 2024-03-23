def solution(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]
    
    ans = 0
    while True:
        tmp = queue.pop(0)
        if any(tmp[1] < q[1] for q in queue):
            queue.append(tmp)
        else:
            ans += 1
            if tmp[0] == location:
                return ans