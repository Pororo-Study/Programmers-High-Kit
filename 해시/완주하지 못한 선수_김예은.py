def solution(participant, completion):
    answer = ''
    # 효율성 통과 못함
    # for i in completion:
    #     if i in participant:
    #         participant.remove(i)
    # answer = participant[0]
    
    participant.sort()
    completion.sort()
    
    for i in range(0, len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            return answer
    answer = participant[-1]
    return answer