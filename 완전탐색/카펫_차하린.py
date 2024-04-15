def solution(brown, yellow):
    answer = []
    
    # a * b = total
    total = brown + yellow
    for b in range(1,total + 1):
        # total / b = a
        # total을 b로 나눈 결과가 정수인지를 확인
        if (total / b) % 1 == 0:
            a = total / b
            # a >= b
            if a >= b:
                # 2*a + 2*b = brown + 4
                if 2*a + 2*b == brown + 4: 
                    return [a,b]
            
    return answer