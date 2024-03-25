from collections import deque   # 큐 자료구조

def solution(priorities, location):
    answer = 0                      # 실행되는 프로세스 count
    q = deque(zip(priorities, range(len(priorities))))  # (중요도, 위치) 형태로 큐에 넣음
    # [(2, 0), (1, 1), (3, 2), (2, 3)]
    
    while q:                        # 큐가 빌때까지 반복
        max_p, _ = max(q)           # 큐에서 중요도의 최댓값
        now_p, now_l = q.popleft()  # 큐 가장 앞에 있는 (현재중요도, 현재위치) 꺼내기
        if now_p == max_p:          # 현재중요도가 최댓값이라면 프로세스 count에 1 더하기
            answer += 1             
            if now_l == location:   # 현재위치가 우리가 알고싶은 위치라면 리턴
                return answer
        else:                       # 현재중요도가 최댓값이 아니라면 큐에 다시 넣기
            q.append((now_p, now_l))