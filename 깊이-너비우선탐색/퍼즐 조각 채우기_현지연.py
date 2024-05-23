# 퍼즐조각을 구하기 위한 DFS
def dfs(x, y, graph, tf, temp_list, n):
    # tf: 보드는 0, 테이블은 1이 퍼즐조각임
    if 0 <= x < n and 0 <= y < n and graph[x][y] == tf:
        graph[x][y] = not(tf)       # 0은 1로, 1은 0으로 바꿈 (방문표시)
        temp_list.append((x, y))
        dfs(x - 1, y, graph, tf, temp_list, n)
        dfs(x, y - 1, graph, tf, temp_list, n)
        dfs(x + 1, y, graph, tf, temp_list, n)
        dfs(x, y + 1, graph, tf, temp_list, n)

# [(x1, y1), (x2, y2), ...] 좌표로 이루어져 있는 퍼즐조각을 0, 1로 채워진 2차원 배열(직사각형)로 만들기   
def make_puzzle(piece_list):
    x_min, x_max, y_min, y_max = 50, 0, 50, 0
    for x, y in piece_list:
        if x < x_min:
            x_min = x
        if x > x_max:
            x_max = x
        if y < y_min:
            y_min = y
        if y > y_max:
            y_max = y
    n = x_max - x_min + 1   # 행의 수
    m = y_max - y_min + 1   # 열의 수
    # 빈공간은 0, 퍼즐이 있는 곳은 1로 채우기
    graph = [[0] * m for _ in range(n)]
    for x, y in piece_list:
        graph[x - x_min][y - y_min] = 1
    # print(piece_list)
    # print(graph)
    return graph
        
# 퍼즐조각(직사각형)을 90도 회전
def rotate(piece):
    # n x m -> m x n 으로 바꾸기
    n = len(piece)
    m = len(piece[0])
    new_piece = [[0] * n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            new_piece[i][j] = piece[n - j - 1][i]
    # print(piece)
    # print(new_piece)
    return new_piece


def solution(game_board, table):
    answer = 0          # 채운 칸 수
    n = len(game_board) # 보드의 크기
    board_list = []     # 보드의 퍼즐 리스트
    table_list = []     # 테이블의 퍼즐 리스트
    
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                # [(x1, y1), (x2, y2), ...] 형태로 퍼즐조각 저장
                board_piece = []
                dfs(i, j, game_board, 0, board_piece, n)
                # 0, 1로 채워진 2차원 퍼즐조각 배열(직사각형) 저장
                board_list.append(make_puzzle(board_piece))
            if table[i][j] == 1:
                table_piece = []
                dfs(i, j, table, 1, table_piece, n)
                table_list.append(make_puzzle(table_piece))
    
    visited = [0] * len(table_list) # 테이블 퍼즐조각을 사용했는지 안했는지 방문표시
    
    # print(board_list)
    # print(table_list)
    
    # 모든 보드퍼즐과 테이블퍼즐을 확인 
    for board_puzzle in board_list:
        for i in range(len(table_list)):
            if visited[i] == 1: # 이미 사용한 테이블퍼즐은 넘김
                continue
            check = False       # 정답여부
            for _ in range(4):
                # 퍼즐조각이 일치하면 채운 칸 수 계산하고 방문처리
                if board_puzzle == table_list[i]:
                    answer += sum(sum(row) for row in board_puzzle)
                    visited[i] = 1
                    check = True
                    break
                # 90도 회전
                table_list[i] = rotate(table_list[i])
            if check:   # 정답이면 다른 퍼즐조각을 확인하지 않고 멈춤
                break
    
    return answer