def solution(command):
    # 위, 오, 아래, 왼: 시계방향
    # 초기방향: +y축
    # +y, +x, -y, -x 방향
    d = 0  
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    x, y = 0, 0
    for c in command:
        if c == 'R':
            d = (d + 1) % 4
        elif c == 'L':
            d = (d - 1) % 4
        elif c == 'G':
            x = x + dx[d]
            y = y + dy[d]
        elif c == 'B':
            x = x - dx[d]
            y = y - dy[d]
    
    return [x, y]