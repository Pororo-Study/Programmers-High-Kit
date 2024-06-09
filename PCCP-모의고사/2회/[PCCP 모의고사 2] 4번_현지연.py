from collections import deque

def solution(n, m, hole):
    answer = int(1e9)
    hole = set(map(tuple, hole))    # hole을 집합으로 변환
    dx = [-1, 1, 0, 0]              # 상하좌우
    dy = [0, 0, -1, 1]
    q = deque([(1, 1, 1, 0)])       # 큐에 (x좌표, y좌표, jump가능여부, 비용) 초기화
    visited = set((1, 1, 1))        # (x좌표, y좌표, jump가능여부)로 방문여부 저장
    
    while q:                            # 큐가 빌 때까지 반복
        x, y, jump, cost = q.popleft()
        
        if x == n and y == m:           # 보물이 있는 칸이면 비용의 최솟값 저장
            answer = min(answer, cost)
        
        for i in range(4):              # 상하좌우로 첫번째 칸 계산
            nx = x + dx[i]
            ny = y + dy[i]
            # 첫번째 칸이 지도를 벗어나지 않은 경우
            if 1 <= nx <= n and 1 <= ny <= m:   
                nnx = nx + dx[i]                # 상상하하좌좌우우로 두번째 칸 계산
                nny = ny + dy[i]
                # 첫번째 칸에 함정이 없는 경우
                if (nx, ny) not in hole and (nx, ny, jump) not in visited:
                    q.append((nx, ny, jump, cost+1))    # 한칸 이동
                    visited.add((nx, ny, jump))
                # 두번째 칸이 지도를 벗어나지 않은 경우
                if 1 <= nnx <= n and 1 <= nny <= m:
                    # 두번째 칸에 함정이 없고 점프를 아직 사용하지 않은 경우
                    if (nnx, nny) not in hole and jump == 1 and (nnx, nny, 0) not in visited:
                        q.append((nnx, nny, 0, cost+1)) # 점프로 두칸이동
                        visited.add((nnx, nny, 0))
                        
    # 보물에 도달하지 못한 경우
    if answer == int(1e9):
        return -1
    # 보물에 도달한 경우
    return answer