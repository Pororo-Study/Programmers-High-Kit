def solution(clothes):
    answer = 1
    # clothes의 각 행은 
    # [의상의 이름, 의상의 종류]
    clo = dict()
    for i in clothes:
        if i[1] in clo:
            clo[i[1]].append(i[0])
        else:
            clo[i[1]] = [i[0]]
    for i in clo.values():
        answer *= (len(i)+1)    

    return answer-1