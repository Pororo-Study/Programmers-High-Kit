from collections import deque

def solution(people, limit):
    answer = 0
    # people리스트를 덱으로 만든 후 내림차순 정렬
    people = deque(sorted(people, reverse=True))
    # 가장 적은 횟수로 사람들을 이동시키려면
    # 제일 무거운 사람, 제일 가벼운 사람을 묶어서 처리
    while len(people) > 1:
        if people[0] + people[-1] <= limit:
            # 최댓값과 최솟값 묶어서 보내줌
            answer += 1
            people.pop() # 최소 빼내고
            people.popleft() # 최대 빼내기
        else:
            answer += 1
            people.popleft() # limit보다 무거우면 무거운 사람만 빼냄
    if people: # people에 1명 남아있는 경우
        answer += 1
        
    return answer