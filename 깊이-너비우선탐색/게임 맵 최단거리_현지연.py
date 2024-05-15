from collections import deque

def solution(maps):
    n = len(maps)       # 행
    m = len(maps[0])    # 열
    
    # 이동할 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque([(0,0)])  # 시작 좌표로 큐 초기화
    
    while q:
        x, y = q.popleft()  # x,y: 현재 좌표
        for i in range(4):  # nx,ny: 다음 좌표
            nx = x + dx[i]  
            ny = y + dy[i]
            # 맵을 벗어난 경우 무시
            if nx < 0 or nx >= n  or ny < 0 or ny >= m:
                continue
            # 해당 좌표를 처음 방문하는 경우에만 최단 거리 기록
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
                
    # 맵의 크기가 1x1일 경우, 0 리턴 
    if n == 1 and m == 1:
        return 0
    # 우측하단 좌표의 값이 1인 경우, 도달하지 못했으므로 -1 리턴
    if maps[n - 1][m - 1] == 1:
        return -1
    # 도달 한 경우, 최단 거리 리턴
    return maps[n - 1][m - 1]