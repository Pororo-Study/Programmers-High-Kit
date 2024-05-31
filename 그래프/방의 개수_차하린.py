from collections import defaultdict

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

def solution(arrows):
    ans = 0
    visit = defaultdict(list)
    
    x, y = 0, 0
    for d in arrows:
        for _ in range(2):
            nx = x + dx[d]
            ny = y + dy[d]
            # 방문했던 점이지만 경로가 겹치지 않는 경우
            if (nx, ny) in visit and (x, y) not in visit[(nx, ny)]:
                ans += 1
                visit[(x, y)].append((nx, ny))
                visit[(nx, ny)].append((x, y))
            elif (nx, ny) not in visit:
                visit[(x, y)].append((nx, ny))
                visit[(nx, ny)].append((x, y))
            x, y = nx, ny                
    
    return ans
    