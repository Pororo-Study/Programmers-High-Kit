from collections import deque   # 큐
from copy import deepcopy       # 깊은 복사

def solution(maze):
    answer = int(1e9)
    n = len(maze)               # 퍼즐판 세로 크기
    m = len(maze[0])            # 퍼즐판 가로 크기
    dx = [-1, 1, 0, 0]          # 상하좌우
    dy = [0, 0, -1, 1]
    
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1: rx, ry = i, j           # 빨간 수레의 시작 칸
            elif maze[i][j] == 2: bx, by = i, j         # 파란 수레의 시작 칸
            elif maze[i][j] == 3: endrx, endry = i, j   # 빨간 수레의 도착 칸
            elif maze[i][j] == 4: endbx, endby = i, j   # 파란 수레의 도착 칸
    
    red_visited = set([(rx, ry)])   # 빨간 수레가 방문한 칸 집합에 저장
    blue_visited = set([(bx, by)])  # 파란 수레가 방문한 칸 집합에 저장
    
    # 빨간수레좌표, 파란수레좌표, 비용, 빨간방문집합, 파란방문집합
    q = deque([(rx, ry, bx, by, 0, red_visited, blue_visited)]) 
    
    while q:
        rx, ry, bx, by, cost, r_visited, b_visited = q.popleft()
        
        # 빨간 수레만 도착했다면, 파란 수레만 움직이기
        if (rx, ry) == (endrx, endry) and (bx, by) != (endbx, endby):
            for i in range(4):      # 파란수레의 다음 좌표
                nbx = bx + dx[i]    
                nby = by + dy[i]
                if 0 <= nbx < n and 0 <= nby < m:   # 격자 판 안에 있는지 검사
                    if maze[nbx][nby] == 5:         # 벽이 아닌지 검사
                        continue
                    if (nbx, nby) == (rx, ry):      # 두 수레가 겹치진 않은지 검사
                        continue
                    if (nbx, nby) not in b_visited: # 방문했던 좌표는 아닌지 검사
                        nb_visited = deepcopy(b_visited)
                        nb_visited.add((nbx, nby))  # 방문기록에 추가
                        q.append((rx, ry, nbx, nby, cost+1, r_visited, nb_visited))
                        
        # 파란 수레만 도착했다면, 빨간 수레만 움직이기
        elif (rx, ry) != (endrx, endry) and (bx, by) == (endbx, endby):
            for i in range(4):      # 빨간수레의 다음 좌표
                nrx = rx + dx[i]
                nry = ry + dy[i]
                if 0 <= nrx < n and 0 <= nry < m:       # 격자 판 안에 있는지 검사
                        if maze[nrx][nry] == 5:         # 벽이 아닌지 검사
                            continue
                        if (nrx, nry) == (bx, by):      # 두 수레가 겹치진 않은지 검사
                            continue
                        if (nrx, nry) not in r_visited: # 방문했던 좌표는 아닌지 검사
                            nr_visited = deepcopy(r_visited)
                            nr_visited.add((nrx, nry))  # 방문기록에 추가
                            q.append((nrx, nry, bx, by, cost+1, nr_visited, b_visited))
                            
        # 둘 다 도착했다면 비용의 최솟값 저장
        elif (rx, ry) == (endrx, endry) and (bx, by) == (endbx, endby):
            answer = min(answer, cost)
            
        # 둘 다 도착하지 않았다면, 수레 둘 다 움직이기
        else:
            for i in range(4):          # 빨간 수레와 파란 수레의 다음 좌표
                for j in range(4):
                    nrx = rx + dx[i]
                    nry = ry + dy[i]
                    nbx = bx + dx[j]
                    nby = by + dy[j]
                    # 격자 판 밖으로 움직일 수 없음
                    if 0 <= nrx < n and 0 <= nry < m and 0 <= nbx < n and 0 <= nby < m:
                        # 동시에 두 수레를 같은 칸으로 움직일 수 없음
                        if (nrx, nry) == (nbx, nby):
                            continue
                        # 벽으로 움직일 수 없음
                        if maze[nrx][nry] == 5 or maze[nbx][nby] == 5:
                            continue
                        # 수레끼리 자리를 바꾸며 움직일 수 없음
                        if (nrx, nry) == (bx, by) and (nbx, nby) == (rx, ry):
                            continue
                        # 자신이 방문했던 칸으로 움직일 수 없음
                        if (nrx, nry) not in r_visited and (nbx, nby) not in b_visited:
                            nr_visited = deepcopy(r_visited)
                            nb_visited = deepcopy(b_visited)
                            nr_visited.add((nrx, nry))
                            nb_visited.add((nbx, nby))
                            q.append((nrx, nry, nbx, nby, cost+1, nr_visited, nb_visited))
    
    # 퍼즐을 풀 수 없는 경우 0을 return
    if answer == int(1e9):
        return 0
                
    return answer