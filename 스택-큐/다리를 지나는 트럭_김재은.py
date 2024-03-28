from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0

    # 0은 무게 때문에 다른 차량이 존재하지 않는 경우를 컨트롤하기 위한 용도
    bridge = deque([0] * bridge_length)
    truck = deque(truck_weights)

    # 다리 위의 존재하는 트럭의 무게를 구하기 위한 변수를 선언
    sum_v = 0

    # 대기 트럭이 빈 상태에서 트럭이 다 빠져나오면 종료
    while bridge:
        answer += 1
        a = bridge.popleft()

        # sum(bridge) 대신 sum_v를 통해서 시간 줄이기
        sum_v -= a

        # 대기 트럭이 없으면,
        if truck:
            # 대기 트럭이 다리에 추가되었을 때, 무게보다 아래면 다리 큐에 트럭 추가
            if sum_v + truck[0] <= weight:
                b = truck.popleft()
                bridge.append(b)
                sum_v += b

            # 무게가 초과되면, 다리 큐에 트럭을 추가하지 않고 0을 추가하여
            # 다리 크기 유지 및 answer 카운트
            else:
                bridge.append(0)

    return answer



"""
def solution(bridge_length, weight, truck_weights):

    answer = 0
    bridge_now = []
    for i, truck in enumerate(truck_weights):

        if sum(bridge_now) + truck <= weight and len(bridge_now) + 1 <= bridge_length:
            bridge_now.append(truck)
        else:
            answer += bridge_length + len(bridge_now) - 1
            bridge_now = [truck]


        # 마지막 원소
        if i == len(truck_weights) - 1:
            answer += bridge_length + len(bridge_now) - 1


    return answer + 1
"""