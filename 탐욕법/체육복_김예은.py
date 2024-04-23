def solution(n, lost, reserve):
    # 여벌 체육복을 가져온 학생도 도난당할 수 있음
    for i in reserve[:]:
        if i in lost: # reserve에 있는 요소가 lost에 있으면 제거
            lost.remove(i)
            reserve.remove(i)
    
    # 정렬
    lost.sort()
    reserve.sort()
    
    # 체육복 빌려주기
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
    
    return n-len(lost)