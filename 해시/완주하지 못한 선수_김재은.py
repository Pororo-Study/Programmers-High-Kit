def solution(participant, completion):

    #완주하지 못한 선수의 이름을 return합니다.
    #동명이인이 있을 수 있습니다.

    #participant와 completion을 비교해야할 것 같다.

    set_participant = set(participant)
    set_completion = set(completion)

    #완주하지 못한 선수가 동명이인이 아닌 경우
    if len(set_participant) - len(set_completion) == 1:
        fail_name = list(set_participant - set_completion)[0]

    #완주하지 못한 선수가 동명이인인 경우
    ###시간초과 ㅠㅠ
    ###remove보다 더 빠른 방법은 뭘까?
    else:
        copy_participant = participant.copy()
        for name in completion:
            copy_participant.remove(name)

        fail_name = copy_participant[0]

    ###index([0])

    return fail_name