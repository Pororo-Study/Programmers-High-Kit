from itertools import permutations

def solution(k, dungeons):
    answer = 0
    dl = len(dungeons)
    
    for dungeon in permutations(dungeons, dl):
        hp = k # 현재 피로도
        count = 0 # 지나온 던전 수
        
        for d in dungeon: # 던전을 돌려면
            if hp >= d[0]: # 최소 필요 피로도는 현재 피로도 보다 같거나 커야함
                hp = hp-d[1] # 던전 돌았으니까 현재 피로도는 소모피로도만큼 증가되고
                count += 1 # 던전 수 증가
                
            if count > answer: # 탐험할 수 있는 최대 던전 수 구하기 위해 비교
                answer = count
    return answer