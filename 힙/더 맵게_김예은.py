import heapq
def solution(scoville, K):
    heapq.heapify(scoville) # scoville 배열 힙으로 변환
    count = 0 # 횟수 체크 변수
    
    # heap의 최솟값 scoville[0]이 기준치 K이상인지 체크(K 이상이면 while 탈출)
    while scoville[0] < K: 
        min_s = heapq.heappop(scoville) # 최소값
        min_s2 = heapq.heappop(scoville) # 두번째 최소값
        heapq.heappush(scoville, min_s+min_s2*2) # 섞은 음식의 스코빌 지수 heap에 추가
        count += 1 # 섞은 횟수 증가
        if len(scoville) == 1 and scoville[0] < K: # 이때 섞을 음식이 1개인데 스코빌 지수가 기준치 K보다 작으면 더이상 섞을 수 없음
            return -1
    return count