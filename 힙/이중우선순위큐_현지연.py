import heapq
def solution(operations):    
    max_h = []  # 최대 힙
    min_h = []  # 최소 힙
    count = 0   # 원소의 개수
    
    for operation in operations:
        c, n = operation.split()    # 명령어, 데이터
        n = int(n)
        # 데이터 추가
        if c == 'I':
            heapq.heappush(max_h, -n)   # 최대 힙에 부호 반대로 삽입
            heapq.heappush(min_h, n)    # 최소 힙에 그대로 삽입
            count += 1                  # 개수 1 더하기
        # 데이터 삭제
        else:
            if n == 1 and max_h:        # 최댓값 삭제
                heapq.heappop(max_h)
            elif min_h:                 # 최솟값 삭제
                heapq.heappop(min_h)
            if len(max_h) + len(min_h) == count:    # 최대힙과 최소힙 초기화
                max_h = []
                min_h = []
                count = 0
    
    # 비어있을 경우, 0 리턴
    if count == 0:
        return [0,0]
        
    # 현재 테스트케이스들을 풀리지만 오류가 있는 코드
    # return [-heapq.heappop(max_h), heapq.heappop(min_h)]
    
    max_h = [-x for x in max_h]         # 최대 힙의 원소들을 원래 부호로 되돌림
    final = set(max_h) & set(min_h)     # 힙을 집합으로 만들고 교집합을 구함
    return [max(final), min(final)]     # 교집합에서 최댓값과 최솟값을 리턴