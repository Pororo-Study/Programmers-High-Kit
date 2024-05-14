from collections import deque   # 큐

def solution(n, computers):
    answer = 0              # 네크워크의 개수
    visited = [0] * n       # 방문 여부
    
    for i in range(n):
        if visited[i] == 1: # 이미 방문 했다면, 넘어가기
            continue
                            # 방문하지 않았다면,
        visited[i] = 1      # 방문 체크
        answer += 1         # 네트워크 개수 추가
        q = deque([i])      # 큐 초기화
        
        while q:            # 큐가 빌 때까지 반복
            now = q.popleft()
            for j in range(n):
                # now와 연결되어있고 방문하지 않았다면, 방문체크하고 큐에 추가  
                if computers[now][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    q.append(j)
    return answer