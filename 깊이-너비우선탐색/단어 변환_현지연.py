from collections import deque
from collections import defaultdict

def solution(begin, target, words):
    n = len(begin)
    visited = {begin}       # 방문한 단어
    dic = defaultdict(set)  # {0: {'h', 'd', 'l', 'c'}, 1:...} 
    
    # 딕셔너리에 데이터 저장
    for word in words:
        for i in range(n):
            dic[i].add(word[i])
            
    # 큐에 (단어, 카운트) 초기화
    q = deque([(begin, 0)])
    
    while q:
        now, cnt = q.popleft()
        if now == target:   # target이라면 카운트 리턴
            return cnt
        for i in range(n):  # 단어의 글자 순서대로 변환
            for change_char in dic[i]:  # 딕셔너리에서 바꿀 수 있는 것으로 변환
                next = now[:i] + change_char + now[i + 1:]  # 변환한 단어
                # word에 있고, 방문하지 않은 단어라면 큐에 추가하고 방문처리
                if next in words and next not in visited:
                    q.append((next, cnt + 1))
                    visited.add(next)
    
    return 0