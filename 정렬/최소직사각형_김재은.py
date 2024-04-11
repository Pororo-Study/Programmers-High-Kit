def solution(sizes):

    #명함의 가로 또는 세로 길이의 최대값을 찾는다.
    #최대값을 가로로 가정하고
    #모든 명함의 가로,세로를 비교하여 더 큰 길이를 가로로 눕혀 수납한다고 가정하자

    #명함의 가로 또는 세로 길이의 최대값을 찾는다.
    w_max = 0
    for size in sizes:
        w, h = size

        if max(w,h) >= w_max:
            w_max = max(w,h)


    #최대값을 가로로 가정
    #모든 명함의 가로 세로를 비교하여 더 큰 길이를 가로로 눕혀 수납한다고 가정
    #명함의 가로 또는 세로 길이의 최소값을 찾는다.
    h_max = 0
    for size in sizes:
        w, h = size

        if min(w,h) >= h_max:
            h_max = min(w,h)
    answer = int(w_max) * int(h_max)

    return answer