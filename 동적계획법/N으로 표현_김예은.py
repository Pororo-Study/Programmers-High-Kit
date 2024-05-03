def solution(N, number):
    if number == 1:
        return 1
    set_list = []
    
    for cnt in range(1, 9): # 1개부터 8개까지 확인(최솟값이 8보다 크면 -1 return)
        partial_set = set() # set 생성
        partial_set.add(int(str(N) * cnt)) # 이어 붙여서 만드는 경우 넣기(5, 55, 555,...)
        for i in range(cnt - 1): # (1, n-1) 부터 (n-1, 1)까지 사칙연산
            for op1 in set_list[i]: # set_list 앞에서 부터
                for op2 in set_list[-i - 1]: # set_list 뒤에서 부터
                    # 중복은 제거됨
                    partial_set.add(op1 + op2)
                    partial_set.add(op1 * op2)
                    partial_set.add(op1 - op2)
                    if op2 != 0:
                        partial_set.add(op1 / op2)
        # 만든 집합에 number가 처음 나오는지 확인
        if number in partial_set:
            return cnt
        set_list.append(partial_set) 
        # [[5], [55, 5+5, 5-5, 5*5, 5/5], [555, 5+ 55, 5* 55, 5- 55, 5/ 55, 5+ 5+5, 5- 5+5, 5* 5+5, 5/ 5+5, 5+ 5-5, 5* 5-5, 5- 5-5..],...]
    return -1
