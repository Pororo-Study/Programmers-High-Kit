import heapq

def solution(operations):
    ans = []
    queue = []
    
    for op in operations:
        x, num = op.split()
        num = int(num)
        
        # 큐에 숫자 삽입
        if x == 'I':
            heapq.heappush(queue, num)
        
        # 큐에서 최댓값 삭제
        elif x == 'D' and num == 1:
            if len(queue) != 0:
                max_value = max(queue)
                queue.remove(max_value)
                
        # 큐에서 최솟값 삭제
        else:
            if len(queue) != 0:
                heapq.heappop(queue)
    
    if len(queue) == 0:
        ans = [0, 0]
    else:
        ans = [max(queue), heapq.heappop(queue)]
        
    return ans