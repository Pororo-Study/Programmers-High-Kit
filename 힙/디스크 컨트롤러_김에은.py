import heapq

def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1 
    heap = []
    
    while i < len(jobs): # 처리한 작업수 i가 jobs의 길이와 같아지면 모든 작업을 처리했다는 의미
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        for j in jobs: # j는 [작업이 요청되는 시점, 작업의 소요시간]
            if start < j[0] <= now: # 처리할 작업이 있는지 확인, 작업이 시작하고 끝날때 까지(작업을 처리할동안) 추가된 작업이 있나 확인
                heapq.heappush(heap, [j[1], j[0]]) # 작업의 소요시간을 기준으로 힙에 추가
        
        if len(heap) > 0: # 처리할 작업이 있는 경우, 작업 처리
            cur = heapq.heappop(heap)
            start = now # start를 now로 갱신(작업 시작 시간 갱신=> now는 현재 시간임)
            now += cur[0] # 작업 소요시간 누적하여 now에 저장, 작업을 처리하면서 시간이 흐름
            answer += now - cur[1] # 현재시간 - 작업 요청시간 => 작업 요청시간부터 종료한 시점까지 시간 계산(대기시간 + 처리시간)
            i +=1 # 작업 처리 수 증가
        else: # 처리할 작업이 없는 경우 다음 시간을 넘어감
            now += 1
                
    return answer // len(jobs) # 작업들이 요청되고 처리되는 시간의 평균
