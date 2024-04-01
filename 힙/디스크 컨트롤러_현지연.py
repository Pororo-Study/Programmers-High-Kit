import heapq

def solution(jobs):
    answer = 0      # 작업의 요청부터 종료까지 기다린 시간 합계
    l = len(jobs)   # 작업의 개수
    
    heapq.heapify(jobs)                         # 리스트를 힙으로 변환
    wait_list  = [(jobs[0][1], jobs[0][0])]     # 현재 시각 기준으로 요청이 들어온 작업 목록. (쇼요시간, 요청시점) 형태
    time = jobs[0][0]                           # 현재 시각 초기화
    heapq.heappop(jobs)                         # 첫번째 작업 삭제
    
    
    while wait_list:    # 요청 목록이 빌 때까지 반복
        
        now = heapq.heappop(wait_list)  # 요청 목록에서 소요시간이 가장 적은 작업 빼내기
        time += now[0]                  # 현재 시각 (종료 시각)
        answer += (time - now[1])       # 요청부터 종료까지 기다린 시간 더하기
        
        # 현재 시각 기준 요청이 들어온 작업들을 요청 목록에 넣기
        while (jobs and jobs[0][0] <= time):                
            req_time, duration = heapq.heappop(jobs)
            heapq.heappush(wait_list, (duration, req_time))
            
        # 현재 시각 기준 요청이 아예 없지만 작업 목록은 아직 남아있을 경우 현재 시각을 다음 요청 시각으로 옮기기
        if not wait_list and jobs:
            req_time, duration = heapq.heappop(jobs)
            heapq.heappush(wait_list, (duration, req_time))
            time = req_time
        
    return answer // l      # 작업의 요청부터 종료까지 걸린 시간 합계를 작업의 개수로 나눔(소수점 이하의 수는 버림)