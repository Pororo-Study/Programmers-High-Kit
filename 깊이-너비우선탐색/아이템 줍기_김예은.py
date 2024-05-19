from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    # board 만들기
    board = [[-1]*102 for _ in range(102)] # 기본값 -1
    
    for r in rectangle:
        # x1 = rectangle[i][0]... 대신
        x1, y1, x2, y2 = map(lambda x: x*2, r) # 2배를 해줘야 인접한 테두리까지 계산 가능
        
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1<i<x2 and y1<j<y2: # 테두리 내부 0
                    board[i][j] = 0
                elif board[i][j] != 0: # 테두리 1
                    board[i][j] = 1
                    

    q = deque()
    q.append([characterX*2, characterY*2])
    visited = [[1]*102 for _ in range(102)] # 101 런타임에러 여유두고 할당

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]


    while q:
        i, j = q.popleft()
        
        # 아이템의 위치에 다다르면 2를 나눈값으로 return
        if i==itemX*2 and j==itemY*2:
            answer = visited[i][j] // 2
            break

        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]

            if board[nx][ny] == 1 and visited[nx][ny] == 1: # visited[nx][ny] == 1이 기본값
                q.append([nx, ny])
                visited[nx][ny] = visited[i][j] + 1
                    
    return answer
