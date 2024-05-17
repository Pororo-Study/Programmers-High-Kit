from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    ans = 0
    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    grid = [[-1] * 102 for _ in range(102)]
    visited = [[1] * 102 for _ in range(102)]

    # 반복문을 마치면 테두리는 1, 내부는 0, 외부는 -1
    for r in rectangle:
        x1, y1, x2, y2 = r[0] * 2, r[1] * 2, r[2] * 2, r[3] * 2
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                # x1, x2, y1, y2는 테두리이므로 제외하고 내부만 0으로 채움
                if x1 < i < x2 and y1 < j < y2:
                    grid[i][j] = 0
                # 직사각형의 내부가 아니면서 테두리라면
                elif grid[i][j] != 0:
                    grid[i][j] = 1

    # 캐릭터와 아이템의 좌표도 2배씩 늘린다
    characterX, characterY, itemX, itemY = characterX*2, characterY*2, itemX*2, itemY*2

    queue = deque([(characterX, characterY)])
    while queue:
        x, y = queue.popleft()

        if x == itemX and y == itemY:
            ans = visited[x][y] // 2
            break

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if grid[nx][ny] == 1 and visited[nx][ny] == 1:
                visited[nx][ny] += visited[x][y]
                queue.append((nx, ny))

    return ans
