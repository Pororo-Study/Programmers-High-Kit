import math
def solution(progresses, speeds):
    answer = []
    release = []
    for i in range(len(progresses)):
        days = math.ceil((100-progresses[i])/speeds[i])
        release.append(days)
    
    tmp = 0
    for i in range(len(release)):
        # 배포가 가능한 날짜 찾기
        if release[tmp] < release[i]:
            answer.append(i-tmp)
            tmp = i
    answer.append(len(release)-tmp)
    return answer
    