from collections import deque

def BFS(begin, target, words):
    queue = deque([(begin, 0)])
    
    while queue:
        now, step = queue.popleft()
        
        if now == target:
            return step
        
        for word in words[:]:
            cnt = 0
            for i in range(len(now)): # 단어의 길이만큼 반복하여
                if now[i] != word[i]: # 단어에 알파벳 한개씩 체크하기
                    cnt += 1
                    
            if cnt == 1:
                words.remove(word)
                queue.append((word, step+1))

def solution(begin, target, words):
    if target not in words : 
        return  0
    
    return BFS(begin, target, words)
