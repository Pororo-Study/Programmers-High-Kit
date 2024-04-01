import heapq    # 최소 힙

def solution(scoville, K):
    h = []  # 힙
    
    # 모든 음식을 힙에 삽입
    for val in scoville:
        heapq.heappush(h, val)
        
    for i in range(0, len(scoville)-1):
        first = heapq.heappop(h)    # 가장 맵지 않은 음식
        if first >= K:              # 가장 맵지 않은 음식이 K이상이라면, 횟수 반환
            return i
        second = heapq.heappop(h)   # 두 번째로 맵지 않은 음식
        mix = first + (second * 2)  # 섞은 음식
        heapq.heappush(h, mix)      # 새로운 음식을 힙에 삽입
    
    # 마지막에 남아있는 음식이 K 이상이라면 횟수 반환
    if h[0] >= K:
        return len(scoville) - 1
    # 모든 음식을 K 이상으로 만들 수 없는 경우에는 -1 반환
    else:
        return -1