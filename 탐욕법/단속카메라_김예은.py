def solution(routes):
    answer = 1
    # 진출지점을 기준으로 오름차순 정렬
    routes.sort(key=lambda x:x[1])
    # 기준을 첫번째 차량의 고속도로 진출 지점으로 잡는다.
    key = routes[0][1]

    # 그 다음 차량이 고속도로로 들어오는 지점과 기준값이 겹치지 않으면
    for i in range(1,len(routes)):
        if key < routes[i][0]:
            answer += 1  # 카메라 수 증가
            key = routes[i][1] # 기준을 그 차량의 진출 지점으로 이동
    return answer