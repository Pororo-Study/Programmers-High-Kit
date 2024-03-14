def solution(clothes):

    #의상 종류/개수
    types = {}
    for line in clothes:
        if line[-1] not in types:
            types[line[-1]] = 0
        types[line[-1]] += 1

    #조합
    answer = 1
    for value in types.values():
        answer = answer * (value + 1)

    return answer - 1