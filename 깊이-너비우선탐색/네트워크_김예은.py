def solution(n, computers):
    answer = 0
    # n 컴퓨터 개수
    # computers 컴퓨터 연결상태
    visited = [0 for _ in range(n)] # 컴퓨터의 방문상태 나타내는 배열
    for com in range(n):
        if visited[com] == 0:
            dfs(visited, n, com, computers) # 방문표시하고 연결상태 확인 
            # 종료 후 하나의 네트워크 확인
            answer += 1
    return answer
def dfs(visited, n, com, computers):
    # 방문표시
    visited[com] = True
    # 연결확인
    for connect in range(n):
        if com != connect and computers[com][connect] == 1: # 연결된 컴퓨터
            if visited[connect] == False: # 방문하지않은 컴퓨터라면
                dfs(visited, n, connect, computers)