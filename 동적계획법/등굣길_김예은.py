def solution(m, n, puddles):
    answer = 0
    # 2차원 배열 만들고(시작점이 [1,1], 도착지가 [m, n])
    grid = [[0] * (m+1) for _ in range(n+1)]
    grid[1][1] = 1 # 시작점 1로
    
    # puddle(문제의 좌표는 (열, 행)임)
    puddles = [[j, i] for [i, j] in puddles]
    
    # 시작점부터 도착지까지 최단경로 계산
    for i in range(1, n+1): 
        for j in range(1, m+1):
            if i==1 and j==1: # 시작점은 통과
                continue
            if [i, j] in puddles: # 물웅덩이면 0
                grid[i][j] = 0
            else: # 위에서 아래로 이동, 왼쪽에서 오른쪽으로 이동 -> 위의 값과 왼쪽값 더함
                grid[i][j] = (grid[i-1][j] + grid[i][j-1])
    return grid[n][m]%1000000007 # 나머지 계산해서 출력