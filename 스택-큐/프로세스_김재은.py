def solution(priorities, location):
    answer = 0

    for _ in priorities:
        ind = priorities.index(max(priorities))
        answer += 1

        if location == ind:
            return answer
        else:
            location = (location-(ind+1)) % len(priorities)

        priorities = priorities[ind+1:] + priorities[:ind]

    return answer
