def DFS(x, computers, visited):
    visited[x] = True
    for i, c in enumerate(computers[x]):
        if c and visited[i] == False:
            DFS(i, computers, visited)

def solution(n, computers):
    ans = 0
    visited = [False] * n
    
    for x in range(n):
        if visited[x] == False:
            DFS(x, computers, visited)
            ans += 1
    return ans
    