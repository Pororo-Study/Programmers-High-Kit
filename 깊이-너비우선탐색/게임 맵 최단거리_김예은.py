from collections import deque
def solution(maps):
    answer = 0
    
    # 상하좌우
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    def bfs(x, y):
        queue = deque()
        queue.append((x, y)) # 튜플 추가
         
        while queue:
            # 꺼내서
            x, y = queue.popleft()
            
            # 상하좌우 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                # 맵을 벗어나면 무시
                if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]):
                    continue
                # 벽이면 무시
                if maps[nx][ny] == 0:
                    continue
                
                # 처음 지나가는 길이면 거리계산하고 다시 상하좌우 확인
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
                    
        return maps[len(maps)-1][len(maps[0])-1]
    
    answer = bfs(0,0)
    return -1 if answer == 1 else answer
    