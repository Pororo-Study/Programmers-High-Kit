import heapq

def solution(jobs):
    # 작업 요청부터 종료까지 걸린 시간 ans
    # 현재 시간 now
    # 처리한 일의 갯수 cnt
    ans, now, cnt = 0, 0, 0
    
    end = -1	#이전 작업 시작 완료 시간
    heap = []
    
    while cnt < len(jobs):
        for job in jobs:
            if end < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])
        if len(heap) > 0:   #처리할 작업이 있는 경우 
            tmp = heapq.heappop(heap)
            # 시작 시간 현재 시간으로 갱신
            end = now     
            # 현재 시간에서 작업 소요 시간을 더해 현재 시간 갱신
            now += tmp[0]
            # 대기 시간 및 처리 시간 누적
            ans += now - tmp[1]
            cnt += 1 # 일 하나 처리했으므로 +1
        
        # 처리할 작업이 없는 경우 현재 시간 1 증가
        else:
            now += 1
    return ans // len(jobs)
