def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            # 왼쪽 끝이니까 제일 첫 번재 더해주기
            if j == 0:
                triangle[i][j] += triangle[i-1][0]
            # 오른쪽 끝이니까 제일 끝 더해주기
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][-1]
            # 나머지 좌 우 중 큰 값 더해주기
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

    return max(triangle[-1])