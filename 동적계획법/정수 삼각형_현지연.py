def solution(triangle):
    
    # 삼각형의 가장자리는 경로가 하나이므로 초기화
    for i in range(1, len(triangle)):
        triangle[i][0] = triangle[i - 1][0] + triangle[i][0]        # 왼쪽 가장자리
        triangle[i][i] = triangle[i - 1][i - 1] + triangle[i][i]    # 오른쪽 가장자리
        
    # (위 또는 왼쪽위) 중에 더 큰 수와 현재 위치의 수 더하기
    for i in range(2, len(triangle)):
        for j in range(1, i):
            triangle[i][j] = max(triangle[i - 1][j], triangle[i - 1][j - 1]) + triangle[i][j]
    
    return max(triangle[len(triangle) - 1]) # 맨 아래 칸 중에 최댓값 리턴