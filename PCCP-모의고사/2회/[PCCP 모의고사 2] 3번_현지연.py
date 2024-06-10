from collections import deque   # 큐

def solution(menu, order, k):
    answer = 0              # 정답
    q = deque()             # 주문 대기
    i = 1                   # 손님 인덱스번호
    t = 0                   # 시각
    now = menu[order[0]]    # 현재 제조하고 있는 음료 남은시간
    customer = 1            # 현재 손님 수
    
    while i < len(order):   # 모든 고객이 주문을 다 할때까지 반복
        t += 1              # 현재 시각 +1
        now -= 1            # 현재 음료 남은시간 차감
        
        if t % k == 0:      # k배수 시각에 손님 도착 후 주문
            q.append(menu[order[i]])
            i += 1
            customer += 1
        
        if now == 0:        # 음료가 완성되면 손님 퇴장
            customer -= 1
        if now <= 0 and q:  # 주문 대기가 있다면 음료 제조시작
            now = q.popleft()
        
        answer = max(answer, customer)  # 현재 손님의 최댓값
        
    return answer