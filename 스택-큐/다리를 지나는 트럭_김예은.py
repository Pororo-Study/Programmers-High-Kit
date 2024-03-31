# 다리에 올라갈 수 있는 트럭 수 bridge_length
# 다리가 견딜 수 있는 무게 weight
# 트럭별 무게 truck_weights

from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    current_w = 0 # 현재 무게
    # truck_weights = deque(truck_weights)
    q = [0]*bridge_length
    while len(truck_weights) > 0:
        answer += 1
        current_w = current_w - q.pop(0)
        # 현재무게 + 다음 트럭무게가 최대하중보다 적으면
        if current_w + truck_weights[0] <= weight:
            current_w += truck_weights[0]
            q.append(truck_weights.pop(0))
        else:
            q.append(0)
            
    answer += bridge_length
    return answer