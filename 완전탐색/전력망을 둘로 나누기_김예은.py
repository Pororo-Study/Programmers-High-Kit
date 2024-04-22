from collections import deque
def solution(n, wires):
    answer = 0
    
    # graph 생성
    graph = [[] for _ in range(n+1)]
    for wire in wires:
        a, b = wire
        graph[a].append(b)
        graph[b].append(a)
        
    def bfs(start):
        visited = [0]*(n+1) 
        queue = deque([start])
        cnt = 1 # 노드 개수 세기
        visited[start] = 1
        
        while queue:
            node = queue.popleft()
            for i in graph[node]:
                if not visited[i]:
                    visited[i] = 1
                    queue.append(i)
                    cnt += 1
            # print(node,queue)
        return cnt
    
    answer = n
    for wire in wires:
        a, b = wire
        # a-b 간선 연결 끊기
        graph[a].remove(b)
        graph[b].remove(a)
        
        # a,b를 시작으로 bfs를 돈 후 각 영역의 노드 개수의 차의 절대값들 중 최소를 구함
        answer = min(abs(bfs(a) - bfs(b)),answer)
        
        # a-b 간선 다시 연결
        graph[a].append(b)
        graph[b].append(a)
        
    return answer