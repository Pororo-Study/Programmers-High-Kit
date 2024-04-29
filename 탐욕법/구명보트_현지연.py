def solution(people, limit):
    answer = 0
    people.sort(reverse=True)   # 내림차순 정렬
    
    start = 0               # 앞 인덱스
    end = len(people) - 1   # 뒤 인덱스
    
    while start <= end:     # start와 end가 교차하면 종료
        answer += 1         # 구명보트 1개 대기중
        # 한 사람만 남았을 경우
        if start == end:
            break
        # 남아있는 사람들 중, 가장 무거운 사람과 가장 가벼운 사람을 같이 태울 수 있는 경우
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
        # 같이 태울 수 없는 경우
        else:
            start += 1
    
    return answer