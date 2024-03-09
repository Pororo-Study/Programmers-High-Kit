def solution(nums):
    N = len(nums)
    H = N // 2
    C = len(set(nums)) # 종류
    if (H >= C) : answer = C 
    else : answer = H
    return answer