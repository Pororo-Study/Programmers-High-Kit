def solution(n, lost, reserve):
    answer = n - len(lost)      # 현재 체육수업을 들을 수 있는 학생 수
    new_lost = []
    
    # 리스트 정렬
    lost.sort()
    reserve.sort()

    # for i in lost:                # 처음에 이렇게 했다가 에러남
    #     if i in reserve:          # lost=[3,4,5], reserve=[3,4,6] 일 경우 에러
    #         reserve.remove(i)     # for문을 돌고있는 배열을 건드리면 안됨!!
    #         lost.remove(i)
    #         answer += 1
    
    # 여벌 체육복을 가져온 학생이 체육복을 도난당한 경우 자기가 써야 함
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            answer += 1
        else:
            new_lost.append(i)
            
    # 왼쪽부터 확인하고 오른쪽 확인
    for i in new_lost:
        if i - 1 in reserve:
            reserve.remove(i - 1)
            answer += 1
        elif i + 1 in reserve:
            reserve.remove(i + 1)
            answer += 1
            
    return answer