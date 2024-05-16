from collections import deque
def solution(begin, target, words):
    answer = 0
    # target이 words에 있는지 검사
    if target not in words:
        return answer
    
    # deque()
    q = deque()
    q.append([begin, 0])
    
    
    while q:
        word, cnt = q.popleft()
        if word == target: # 종료
            answer = cnt
            return answer
        for i in range(len(words)): # 단어마다
            temp_cnt = 0
            for j in range(len(word)): # 단어의 한 문자씩 검사
                if word[j] != words[i][j]:
                    temp_cnt += 1
            if temp_cnt == 1: # 차이가 1이면 다음문자로 변환
                q.append([words[i],cnt+1])
