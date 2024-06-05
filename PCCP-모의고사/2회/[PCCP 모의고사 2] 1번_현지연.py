def solution(command):
    x, y, d = 0, 0, 0   # x좌표, y좌표, 방향
    
    dx = [0, 1, 0, -1]  # 상, 우, 하, 좌
    dy = [1, 0, -1, 0]
    
    for c in command:
        if c == 'R':        # 오른쪽 회전
            d = (d + 1) % 4
        elif c == 'L':      # 왼쪽 회전
            d = (d + 3) % 4
        elif c == 'G':      # 전진
            x += dx[d]
            y += dy[d]
        else:               # 후진
            x -= dx[d]
            y -= dy[d]

    return [x, y]