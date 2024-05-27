def solution(distance, rocks, n):
    rocks.sort()    # 바위 정렬
    
    # 거리 배열
    arr = [rocks[0]]    # 거리 배열 초기화 (시작지점과 첫번째바위의 거리)
    for i in range(len(rocks) - 1):
        arr.append(rocks[i+1] - rocks[i])
    arr.append(distance - rocks[-1])    # 마지막 바위와 도착지점의 거리
    
    # 이분탐색
    start = 1       # 최소 거리       
    end = distance  # 최대 거리
    
    while start <= end:
        # mid를 '거리의 최솟값 기준'으로 생각하고 바위를 지워보자
        mid = (start + end) // 2    
        remove_cnt = 0      # 제거한 바위의 수
        sum_val = 0         # 바위 사이의 거리
        for elem in arr:
            sum_val += elem
            # 바위 사이의 거리가 mid 보다 작으면, 바위 제거
            if sum_val < mid:
                remove_cnt += 1
            # 바위 사이의 거리가 mid 보다 크거나 같으면 바위를 냅둠 -> 거리 초기화
            else:
                sum_val = 0
        # 제거한 바위의 수가 n보다 작거나 같으면 mid 저장하고 오른쪽 탐색
        if remove_cnt <= n:
            answer = mid
            start = mid + 1
        # 제거한 바위의 수가 n보다 크다면 왼쪽 탐색
        elif remove_cnt > n:
            end = mid - 1
            
    return answer