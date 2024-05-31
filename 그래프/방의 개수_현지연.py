def solution(arrows):
    answer = 0
    visit_xy = set()    # 방문한 좌표
    visit_line = set()  # 방문한 선분
    
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    
    # 시작 좌표 초기화
    x, y = 0, 0
    visit_xy.add((x, y))

    for i in arrows:
        for _ in range(2):      # 대각선인 경우를 위해 2번 반복
            nx = x + dx[i]      # 다음 좌표
            ny = y + dy[i]
            # 이미 방문한 좌표지만, 중복된 선분이 아닌 경우 
            if (nx, ny) in visit_xy and ((x,y),(nx,ny)) not in visit_line:
                answer += 1     # 방 증가
            # 좌표, 선분, 반대선분 방문처리
            visit_xy.add((nx, ny))
            visit_line.add(((x,y),(nx,ny)))
            visit_line.add(((nx,ny),(x,y)))
            x, y = nx, ny   # 좌표 변경

    return answer