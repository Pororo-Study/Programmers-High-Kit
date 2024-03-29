def solution(prices):
    answer = [0] * len(prices) # [0, 0, 0, 0, 0]
    # 그 가격이 얼마나 버텼는지 계산
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            answer[i] += 1 # 떨어진 경우에도 1초 버텼다고 생각
            if prices[i] > prices[j]:
                break
        
    
    return answer