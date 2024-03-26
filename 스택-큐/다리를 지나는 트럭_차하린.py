from collections import deque

def solution(bridge_length, weight, truck_weights):
    ans = 0     # 시간
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    
    tmp = 0     # 전체 무게 관리
    while len(bridge):
        ans += 1
        tmp -= bridge[0]
        bridge.popleft()
        
        if truck_weights:
            if tmp + truck_weights[0] <= weight:
                tmp += truck_weights[0]
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)
    
    return ans