def judge(mid, n, times):
    # 모든 심사대에서 mid분 동안 심사할 수 있는
    # 최대 인원을 모두 더함
    # 이 값이 n 이상이면 True 아니면 False
    if sum([mid // x for x in times]) >= n:
        return True
    return False

def solution(n, times):
    ans = 0
    times.sort()
    
    start, end = 1, times[-1] * n
    while start <= end:
        mid = (start + end) // 2
        result = judge(mid, n, times)
        
        # mid분 동안 모든 사람을 심사할 수 있다면,
        # mid보다 더 적은 시간동안 모든 사람을 심사할 수
        # 있는지를 알아봐야하므로 구간을 작은 쪽으로 좁혀주기
        if result:
            end = mid - 1
        else:
            start = mid + 1
    
    return start
    