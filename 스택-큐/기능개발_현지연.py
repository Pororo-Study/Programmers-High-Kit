import math

def solution(progresses, speeds):
    answer = []
    count = 1       # 한 번에 배포하는 기능 개수
    start = math.ceil((100 - progresses[0]) / speeds[0])    # 배포 기준: 각 배포 맨 앞에 있는 기능의 작업 일 수
    
    for i in range(1, len(progresses)):
        now = math.ceil((100 - progresses[i]) / speeds[i])  # 작업 일 수
        # 배포 기준보다 작으면 같이 배포
        if start >= now:
            count += 1
        # 배포 기준보다 크면 따로 배포
        else:
            start = now             # 배포 기준 업데이트
            answer.append(count)
            count = 1
    
    # 배포할 기능이 남아있다면 배포
    if count > 0:
        answer.append(count)
    
    return answer