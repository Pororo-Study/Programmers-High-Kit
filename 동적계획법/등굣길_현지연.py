def solution(m, n, puddles):
    graph = [[0] * m for _ in range(n)] # 각 좌표에 경로의 개수 저장
    
    # 왼쪽 줄 1로 초기화
    for i in range(n):
        # 웅덩이가 나오면 멈춤
        if [1, i + 1] in puddles:
            break
        graph[i][0] = 1
    
    # 위쪽 줄 1로 초기화
    for j in range(m):
        # 웅덩이가 나오면 멈춤
        if [j + 1, 1] in puddles:
            break
        graph[0][j] = 1
        
    # 나머지 좌표 계산
    for i in range(1, n):
        for j in range(1, m):
            if [j + 1, i + 1] not in puddles:
                graph[i][j] = graph[i - 1][j] + graph[i][j - 1] # 왼쪽과 위쪽 숫자 더함
                
    return graph[n - 1][m - 1] % 1000000007