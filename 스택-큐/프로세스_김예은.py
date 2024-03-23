import queue
def solution(priorities, location):
    answer = 0
    q = queue.Queue()
    index = queue.Queue()
    l = sorted(priorities) # 오름차순 정렬
    
    for i, j in enumerate(priorities):
        q.put(j) # 우선순위
        index.put(i) # 인덱스
    
    c = 1
    while q.qsize() > 0:
        # 일단 꺼내
        x = q.get()
        y = index.get()
        
        # 우선순위 맞는지 확인
        if x == l[-1]:
            # 맞으니까 다음 우선순위로 가야해서 pop()
            l.pop()
            # 찾고있는 프로세스인지 인덱스 확인
            if y == location:
                # 정렬 후 그 프로세스의 위치 반환
                return c
            c += 1
        else:
            # 다시 넣음
            q.put(x)
            index.put(y)
    
    
    return answer