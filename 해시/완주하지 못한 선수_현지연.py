# # 풀이 1
# def solution(participant, completion):
#     answer = ''
    
#     participant.sort()  # 참여 명단 정렬 O(N log N)
#     completion.sort()   # 완주 명단 정렬 O(N log N)
    
#     for i in range(len(completion)):            # 완주 명단 배열의 길이만큼 반복
#         if participant[i] != completion[i]:     # 참여와 완주 명단을 비교
#             answer = participant[i]
#             break
            
#     # 완주 명단을 다 확인해도 정답이 없다면, 참여 명단의 마지막 사람이 완주하지 못했다는 뜻
#     if not answer:
#         answer = participant[-1]
        
#     return answer

# 풀이 2
from collections import defaultdict # 값(value)에 초깃값을 지정하여 딕셔너리를 생성하는 모듈
def solution(participant, completion):
    answer = ''
    
    par = defaultdict(int)  # 참여 명단 딕셔너리
    comp = defaultdict(int) # 완주 명단 딕셔너리

    # key-value: 선수이름-명수를 딕셔너리에 저장
    for elem in participant:
        par[elem] += 1
    for elem in completion:
        comp[elem] += 1 
        
    # 선수 이름으로 명수를 비교해서 다르면 정답 
    for elem in list(par.keys()):
        if par[elem] != comp[elem]:
            answer = elem
            break
    
    return answer