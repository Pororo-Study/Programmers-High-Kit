import heapq

def solution(program):
    # return 해야 하는 answer 배열은 길이가 11인 정수 배열
    answer = [0] * 11
    # 프로그램 점수, 호출된 시각, 실행 시간을 의미
    # 호출된 시각 -> 점수 낮은 순으로 정렬
    program.sort(key = lambda x : (x[1], x[0]))
    
    heap = []   # 대기 중인 프로그램을 대기 큐에 추가
    cur = 0     # 현재 시각?
    
    idx = 0
    n = len(program)
    
    while idx < n or heap:
        while idx < n and program[idx][1] <= cur:
            heapq.heappush(heap, (program[idx][0], program[idx][1], program[idx][2]))
            idx += 1
        
        if heap:
            # 우선순위가 가장 높은 프로그램을 실행합니다.
            priority, time, duration = heapq.heappop(heap)
            if cur < time:
                cur = time
            answer[priority] += cur - time
            cur += duration
        else:
            # 대기 큐가 비어 있는 경우, 다음 프로그램 호출 시각으로 이동합니다.
            if idx < n:
                cur = program[idx][1]
            
    answer[0] = cur
            
    return answer