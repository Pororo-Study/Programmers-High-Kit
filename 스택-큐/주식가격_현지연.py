def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            # 가격이 떨어졌거나 끝까지 가격이 떨어지지 않았을 경우 j-i 입력
            if prices[i] > prices[j] or j == len(prices) - 1:   
                answer.append(j - i)
                break
            
    answer.append(0)    # 마지막은 값은 무조건 0            
    return answer