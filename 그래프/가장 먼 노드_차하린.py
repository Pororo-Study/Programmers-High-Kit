from collections import deque 
from collections import defaultdict

def solution(n, edge):
    graph = defaultdict(list)
    visited = [0] * (n + 1)
    
    for e, v in edge:
        graph[e].append(v)
        graph[v].append(e)
        
    queue = deque()
    queue.append(1)
    visited[1] = 1
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = visited[x] + 1 
                queue.append(i)
    
    max_value = max(visited)   
    return visited.count(max_value)