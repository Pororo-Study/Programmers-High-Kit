from collections import deque

def solution(numbers, target):
    ans = 0
    queue = deque()
    queue.append((0, 0))
    
    while queue:
        now, idx = queue.popleft()
        if idx < len(numbers):
            queue.append((now + numbers[idx], idx + 1))
            queue.append((now - numbers[idx], idx + 1))
        elif idx == len(numbers):
            if now == target:
                ans += 1
    return ans
    