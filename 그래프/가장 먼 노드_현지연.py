from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for i in range(n + 1)]  # 그래프 인접 리스트 표현
    distance = [50000] * (n + 1)        # 거리 배열

    # 연결 정보 저장 (양방향 그래프)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    q = deque([1])  # 큐를 시작 노드로 초기화
    distance[1] = 0 # 시작 노드의 거리는 0
    
    # BFS
    while q:
        v = q.popleft()
        for i in graph[v]:
            cost = distance[v] + 1
            # 더 짧은 거리값 저장 
            if cost < distance[i]:
                distance[i] = cost
                q.append(i)
        
    # 최대 거리인 노드 개수 구하기
    max_val = max(distance[1:]) # distance[0]은 50000이므로 제외해야함
    for d in distance:
        if d == max_val:
            answer += 1
    
    return answer