def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    t1 = h1 * 3600 + m1 * 60 + s1   # 시작 시간
    t2 = h2 * 3600 + m2 * 60 + s2   # 종료 시간
    
    # 시작 시간이 0시0분0초 또는 12시0분0초일 경우, 겹침
    if t1 == 0 * 3600 or t1 == 12 * 3600:
        answer += 1
    
    while t1 < t2:
        # 현재 시간 각도
        h_angle = t1 / 120 % 360    # 시침은 1초에 1/120도 움직임
        m_angle = t1 / 10 % 360     # 분침은 1초에 1/10도 움직임
        s_angle = t1 * 6 % 360      # 초침은 1초에 6도 움직임
        # 1초 후 각도
        nh_angle = (t1 + 1) / 120 % 360
        nm_angle = (t1 + 1) / 10 % 360
        ns_angle = (t1 + 1) * 6 % 360        
        # 1초 후 각도가 0도가 되면 전과 후를 계산할 수 없기 때문에 360도로 만들어줌
        if nh_angle == 0:           
            nh_angle = 360
        if nm_angle == 0:
            nm_angle = 360
        if ns_angle == 0:
            ns_angle = 360
        # 초가 변하는 사이에 초침이 시침과 겹친다면 횟수 더하기
        if s_angle < h_angle and ns_angle >= nh_angle:
            answer += 1
        # 초가 변하는 사이에 초침이 분침과 겹치고 분침이 시침과 겹치지 않는다면 횟수 더하기
        if s_angle < m_angle and ns_angle >= nm_angle and nh_angle != nm_angle:
            answer += 1
        # 초 변환
        t1 += 1
                
    return answer