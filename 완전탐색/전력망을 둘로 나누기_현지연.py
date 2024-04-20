import heapq

# 송전탑 개수의 차이를 반환하는 함수
# BFS 방식
def calculate(graph, n):
    num = []
    q = []
    visited = [0] * (n + 1)     # 방문 여부
    for i in range(1, n + 1):
        cnt = 0                 # 개수
        if visited[i] == 0:
            heapq.heappush(q, i)
            visited[i] = 1
            cnt += 1
            while q:
                now = heapq.heappop(q)
                for x in graph[now]:
                    if visited[x] == 0:
                        heapq.heappush(q, x)
                        visited[x] = 1
                        cnt += 1  
        if cnt > 0:
            num.append(cnt)
    return max(num) - min(num)
    

def solution(n, wires):
    answer = 100
    graph = [set() for _ in range(n + 1)]
    
    # 인접 리스트 방식으로 트리를 표현
    for v1, v2 in wires:
        graph[v1].add(v2)
        graph[v2].add(v1)
        
    # [v1, v2]를 끊어서 송전탑 개수의 차이 구하기
    for v1, v2 in wires:
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        answer = min(answer, calculate(graph, n))
        graph[v1].add(v2)
        graph[v2].add(v1)
        
    return answer