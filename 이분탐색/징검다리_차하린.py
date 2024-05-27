def solution(distance, rocks, n):
    ans = 0
    
    left = 1
    right = distance
    
    rocks.sort()
    rocks.append(distance)
    
    while left <= right:
        mid = (left +  right) // 2
        
        cnt = 0     # 바위 제거 횟수
        prev = 0    # 이전 바위 위치
        for rock in rocks:
            # 각 바위 사이 거리
            dist = rock - prev
            
            # 거리가 커트라인보다 작으면 삭제
            if dist < mid:
                cnt += 1
                if cnt > n:
                    break
            # 바위 삭제 안했으므로 이전 바위 업데이트
            else:
                prev = rock
        
        # n개의 바위를 제거해야하는데 그거보다 크다면
        # 현재 값 기준으로 값이 더 낮아야 바위를 n보다 적게 제거 가능
        if cnt > n:
            right = mid - 1
        # 제거된 바위의 개수가 n개 이하라면, 더 제거하여, 더 큰 최솟값을 바랄 수 있음
        else:
            ans = mid
            left = mid + 1
    
    return ans
        