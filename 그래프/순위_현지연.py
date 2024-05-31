# 플로이드 워셜 알고리즘
def solution(n, results):
    answer = 0
    INF = int(1e9)
    graph = [[INF] * (n + 1) for _ in range(n + 1)] # 그래프 초기화
    
    # 자기자신으로 가는 경우는 0
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0
    
    # a에서 b로 가는 거리는 1
    for a, b in results:
        graph[a][b] = 1
        
    # 최단거리 계산
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    
    # i가 다른 모든 숫자와 관계가 있으면 순위를 매길 수 있음
    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, n + 1):
            if 0 < graph[i][j] < INF or  0 < graph[j][i] < INF:
                cnt += 1
        if cnt == n - 1:
            answer += 1
    return answer