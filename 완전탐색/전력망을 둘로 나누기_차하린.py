from collections import deque
def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    def BFS(start):
        visited = [0] * (n + 1)
        queue = deque([start])
        visited[start] = 1
        cnt = 1
        
        while queue:
            tmp = queue.popleft()
            for i in graph[tmp]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = 1
                    cnt += 1
        return cnt
    
    res = n
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        res = min(abs(BFS(a) - BFS(b)), res)
                  
        graph[a].append(b)
        graph[b].append(a)
  
    return res