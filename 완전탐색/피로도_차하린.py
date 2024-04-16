from itertools import permutations

def solution(k, dungeons):
    ans = 0
    dun_num = len(dungeons)
    
    for order in permutations(dungeons, dun_num):
        life = k
        cnt = 0
        
        for x in order:
            if life >= x[0]:
                life -= x[1]
                cnt += 1
        if cnt > ans:
            ans = cnt
    return ans