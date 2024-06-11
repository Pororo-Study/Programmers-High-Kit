import heapq
def solution(ability, number):
    queue =  []
    for a in ability:
        heapq.heappush(queue, a)
    
    for _ in range(number):
        a = heapq.heappop(queue)
        b = heapq.heappop(queue)
        
        tmp = a + b
        heapq.heappush(queue, tmp)
        heapq.heappush(queue, tmp)
    
    return sum(queue)
    