from collections import deque

# 모든 좌표에 2를 곱할 예정
def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[0] * 101 for _ in range(101)]     # 그래프
    
    # 직사각형의 테두리를 1로 표시
    for rec in rectangle:
        x1, y1, x2, y2 = rec[0] * 2, rec[1] * 2, rec[2] * 2, rec[3] * 2
        for i in range(x1, x2 + 1):
            graph[i][y1] = 1
            graph[i][y2] = 1
        for j in range(y1, y2 + 1):
            graph[x1][j] = 1
            graph[x2][j] = 1
            
    # 직사각형의 안쪽을 1로 표시
    for rec in rectangle:
        x1, y1, x2, y2 = rec[0] * 2, rec[1] * 2, rec[2] * 2, rec[3] * 2
        for i in range(x1 + 1, x2):
            for j in range(y1 + 1, y2):
                graph[i][j] = 2
                
    # 이동할 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque([(characterX * 2, characterY * 2)])   # 시작좌표로 큐 초기화
    graph[characterX * 2][characterY * 2] = 0       # 시작좌표의 거리를 0으로 초기화
    
    while q:
        x, y = q.popleft()                  # x,y: 현재 좌표
        if x == itemX * 2 and y == itemY * 2:
            return graph[x][y] // 2         # 모든 좌표를 2 곱했으므로 거리도 2로 나눠줘야 함
        for i in range(4):                  # nx,ny: 다음 좌표                  
            nx = x + dx[i]
            ny = y + dy[i]
            # 좌표가 범위를 벗어나지 않았고, 아직 방문하지 않은 테두리라면
            if 2 <= nx <= 100 and 2 <= ny <= 100 and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1     # 현재까지 거리 계산
                q.append((nx, ny))                  # 큐에 넣기