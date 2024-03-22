def solution(progresses, speeds):

    answer = []

    #뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포될 수 있다.
    while len(progresses) != 0:
        #progresses 복사
        copy_progresses = progresses.copy()

        #progresses가 며칠 뒤에 100 이상일까? 그리고 몇개가 있을까?
        for day in range(1,100):
            if copy_progresses[0] + speeds[0] * day >= 100:
                d = day
                break

        for i in range(len(copy_progresses)):
            copy_progresses[i] = copy_progresses[i] + speeds[i] * day

        #배포될 기능을 담을 result, progresses와 speed에서 result만큼 pop
        result = 0
        for progress in copy_progresses:
            if progress >= 100:
                result += 1
                progresses.pop(0)
                speeds.pop(0)
            else:
                break

        #result를 answer에 담는다.
        answer.append(result)

    return answer