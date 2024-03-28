from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0                      # 초
    i = 0                           # 인덱스
    q = deque()                     # 다리 큐
    
    # 대기 트럭이 없을때 까지 반복
    while i < len(truck_weights):
        now_weight = 0                          # 현재 다리 위 무게
        
        # 현재 다리 위에 있는 트럭들의 위치를 업데이트, 다리 위 무게 구하기
        for _ in range(len(q)):
            truck, location = q.popleft()
            if location < bridge_length:
                q.append((truck, location + 1))
                now_weight += truck
                
        # 대기 트럭이 다리에 올라갈 수 있다면 큐에 추가
        if len(q) < bridge_length and now_weight + truck_weights[i] <= weight:
            q.append((truck_weights[i], 1))
            i += 1      # 인덱스 업데이트
        
        answer += 1     # 초 업데이트
    
    # 마지막 대기 트럭까지 다리에 올랐다면, 그 트럭이 다리를 다 건넌 시간 반환
    return answer + bridge_length