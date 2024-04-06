import heapq
def solution(operations):
    min_heap = [] # 최소힙
    max_heap =  [] # 최대힙
    for op in operations:
        c, num = op.split() # 문자와 숫자 분리
        if c == 'I':
            heapq.heappush(min_heap, int(num))
            heapq.heappush(max_heap, -int(num)) # 최대힙에 추가시 -를 붙여 추가. [0]가 최대값이 오도록함
        elif c == 'D':
            if not max_heap: # 힙이 비었으면 pass(min_heap해도 상관없음)
                pass
            elif num == '1': # 최대값 삭제
                x = heapq.heappop(max_heap)
                min_heap.remove(-x) # 최대힙을 만들기 위해 -붙여서 min_heap에서 찾을 때도 -붙여서 양수 만들고 난 후 찾음
            
            elif num == '-1': # 최소값 삭제
                x = heapq.heappop(min_heap)
                max_heap.remove(-x) # 최대힙에서 heapq.heappop() 한다면 음수형태이므로 min_heap에서 찾기 위해 -붙임
    return [-heapq.heappop(max_heap), heapq.heappop(min_heap)] if max_heap else [0,0]
    # 최대힙은 -붙여 최대힙을 구현했으므로 출력 시 다시 -붙여서 출력, 조건식에 max_heap이나 min_heap 상관없음