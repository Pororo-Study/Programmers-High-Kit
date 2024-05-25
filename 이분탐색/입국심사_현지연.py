def solution(n, times):
    answer = 0
    
    # 이분탐색
    start = 1               # 정답이 될 수 있는 최솟값
    end = n * 1000000000    # 정답이 될 수 있는 최댓값

    while start <= end:
        # 모든 사람이 심사를 받는 데 mid분 이내로 걸릴 수 있는지 판단
        mid = (start + end) // 2    # 중간 값
        cnt = 0                     # mid분 이내에 심사를 받을 수 있는 사람은 cnt명
        for t in times:
            cnt += mid // t
        # cnt가 n보다 크거나 같으면, 일단 mid를 저장하고 더 작은 mid 확인
        if cnt >= n:
            answer = mid
            end  = mid - 1
        # cnt가 n보다 작으면, 더 큰 mid 확인
        else:
            start = mid + 1
    
    return answer