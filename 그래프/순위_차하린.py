from collections import defaultdict

def solution(n, results):
    answer = 0
    win = defaultdict(set)
    lose = defaultdict(set)
    
    for winner, loser in results:
        # loser을 이긴
        win[loser].add(winner)
        # winner에게 진
        lose[winner].add(loser)
        
    for i in range(1, n+1):
        # i한테 진 애들은 i를 이긴 애들한테도 진 것
        # i한테 이긴 애들은 i한테 진 애들한테도 이긴 것
        for winner in win[i]:
            lose[winner].update(lose[i])
        for loser in lose[i]:
            win[loser].update(win[i])
        
    # i한테 이기고 진 애들 합쳐서 n-1이면 순위가 결정된 것
    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n-1:   
            answer += 1
    
    return answer