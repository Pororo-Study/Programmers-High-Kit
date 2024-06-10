def solution(queries):
    answer = []
    
    for n, p in queries:
        nth = (p - 1) % 4 + 1   # 부모의 몇번째 자식인지 계산
        stack = [(n, p, nth)]   # (세대, 몇 번째 개체인지, 부모의 몇번째 자식인지)를 스택에 저장
        
        # 2세대까지 올라가면서 스택에 저장
        for i in range(1, n - 1):
            p = (p - 1) // 4 + 1
            nth = (p - 1) % 4 + 1
            stack.append((n - i, p, nth))
        
        # 2세대 ~ n세대까지 내려가면서 형질 찾기 
        pea = "Rr"  # 1대 초기화
        for i in range(n - 2, -1, -1):
            if pea == "Rr":
                if stack[i][2] == 1:    # 부모가 Rr이고 부모의 1번째 자식일 때, RR
                    pea = "RR"
                elif stack[i][2] == 4:  # 부모가 Rr이고 부모의 4번째 자식일 때, rr
                    pea = "rr"
                
        answer.append(pea)  # 최종 형질 저장
    
    return answer