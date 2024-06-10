from itertools import permutations

def solution(ability):
    answer = 0
    
    student = len(ability)
    sport = len(ability[0])
    
    idx = list(range(student))
    for perm in permutations(idx, sport):
        tmp = 0
        for i in range(sport):
            tmp += ability[perm[i]][i]
        
        answer = max(answer, tmp)

    return answer