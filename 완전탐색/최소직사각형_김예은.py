def solution(sizes):
    # answer = 0
    w = [] # 가로
    h = [] # 세로
    for i in sizes:
        # i[0], i[1]중 긴 것은 가로, 짧은 것은 세로에 넣어줌
        w.append(max(i)) # i는 2개의 원소밖에 없으므로 최댓값을 가로에 넣어줌
        h.append(min(i)) # 나머지 하나는 자동으로 최솟값. 세로에 넣어줌
    return max(w)*max(h) # 가장 긴 가로와 세로를 구해 모든 명함이 들어가게 함.