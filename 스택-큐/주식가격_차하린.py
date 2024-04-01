from collections import deque

def solution(prices):
    prices = deque(prices)
    ans = []
    
    while prices:
        price = prices.popleft()
        sec = 0
        for queue in prices:
            sec += 1
            if price > queue:
                break
        ans.append(sec)
    return ans