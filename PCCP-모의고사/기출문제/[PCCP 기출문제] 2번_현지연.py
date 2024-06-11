from collections import deque
def solution(land):
    answer = 0
    n = len(land)       # 땅의 세로 길이
    m = len(land[0])    # 땅의 가로 길이
    idx = 2             # 석유 덩어리를 구분하기 위한 인덱스 번호
    oil = [0, 0]        # oil[idx]는 idx번호의 석유 덩어리의 크기
    dx = [-1, 1, 0, 0]  # 상하좌우
    dy = [0, 0, -1, 1]
    
    for j in range(m):          # 세로로 순회하기
        for i in range(n):
            if land[i][j] == 1:     # 석유가 있는 땅이라면
                # BFS로 석유 덩어리의 크기 구하기
                q = deque([(i, j)])
                land[i][j] = idx    # 석유 덩어리를 구분하기 위한 인덱스 번호
                count = 1           # 석유 덩어리의 크기 count
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1:
                            land[nx][ny] = idx
                            count += 1
                            q.append((nx, ny))
                oil.append(count)   # 덩어리의 크기를 구했다면 oil 배열에 저장하기
                idx += 1
    
    for j in range(m):  # 세로로 순회하기
        # 어떤 석유 덩어리가 있는지 set에 인덱스 번호 저장하기
        oil_idx = set() 
        for i in range(n):
            if land[i][j] > 0:
                oil_idx.add(land[i][j])
        # 석유 덩어리 크기의 총합 구하기
        oil_total = 0
        for idx in oil_idx:
            oil_total += oil[idx]
        # 최댓값 구하기
        answer = max(answer, oil_total)    
                
    return answer