import heapq    # 최소 힙  # 우선순위 큐

def solution(ability, number):
    heapq.heapify(ability)  # 기존 리스트를 힙으로 변환
    
    for _ in range(number):
        a = heapq.heappop(ability)  # 최솟값 추출
        b = heapq.heappop(ability)  # 두번째 최솟값 추출
        heapq.heappush(ability, a + b)  # 능력치의 합 삽입
        heapq.heappush(ability, a + b)  # 능력치의 합 삽입
        
    return sum(ability) # 모든 신입사원들의 능력치의 합