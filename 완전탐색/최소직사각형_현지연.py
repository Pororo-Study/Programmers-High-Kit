def solution(sizes):
    w = [x[0] for x in sizes]   # 가로 길이를 원소로 가지는 배열
    h = [x[1] for x in sizes]   # 세로 길이를 원소로 가지는 배열
    
    max_a = max(max(w), max(h)) # 모든 숫자 통틀어서 최댓값
    max_b = 0
    
    for i in range(len(w)):        
        max_b = max(max_b, min(w[i], h[i])) 
        
    return max_a * max_b