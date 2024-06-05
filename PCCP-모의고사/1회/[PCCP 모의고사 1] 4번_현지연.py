import heapq    # 힙을 사용해 우선순위 큐 구현

def solution(program):
    answer = [0] * 11
    t = 0   # 시각
    i = 0   # program 인덱스
    h = []  # 힙
    program.sort(key=lambda x: (x[1], x[0]))    # 호출시각, 점수 순으로 정렬
    
    while i < len(program) or h:
        # 현재시각 기준 호출된 프로그램이라면 힙에 추가
        if i < len(program) and program[i][1] <= t:     
            heapq.heappush(h, program[i])
            i += 1
        # 현재시각 기준 호출되지도 않았고, 힙도 비어있다면 바로 실행 
        elif not h:
            t = program[i][1] + program[i][2]
            i += 1
        # 현재시각 기준 호출된 프로그램이 다 힙에 들어왔다면, 우선순위큐(최소힙)에서 점수가 낮은 프로그램 실행
        else:
            score, calltime, runtime = heapq.heappop(h)
            answer[score] += t - calltime   # 대기시간 추가
            t += runtime
            
    answer[0] = t   # 종료시각
    return answer