from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    # 순열을 사용해 모든 경우의 수 탐색
    for case in list(permutations(dungeons, len(dungeons))):
        count = 0                       # 탐험한 던전 수
        health = k                      # 현재 피로도
        for require, consume in case:
            if health >= require:       # 현재 피로도가 최소 필요 피로도 이상이라면
                health -= consume       # 피로도 소모하기
                count += 1              # 던전 수 증가
        answer = max(count, answer)     # 최댓값 계산
    
    return answer