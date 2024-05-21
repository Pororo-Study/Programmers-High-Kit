from collections import defaultdict

def solution(tickets):
    routes = defaultdict(list)
    
    for (start, end) in tickets:
        routes[start].append(end)
    
    for port in routes:
        routes[port].sort(reverse = True)
    
    path = []
    stack = ["ICN"]
    while stack:
        tmp = stack[-1]
        if not routes[tmp]:
            path.append(stack.pop())
        else:
            next = routes[tmp].pop()
            stack.append(next)
    
    return path[::-1]
    