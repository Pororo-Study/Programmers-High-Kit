def solution(input_string):
    answer = []
    dic = dict()    # 딕셔너리 생성 (key는 알파벳, value는 인덱스)
    
    for i in range(len(input_string)):
        x = input_string[i]
        
        if x not in dic:        # 처음 나타난 알파벳은 인덱스 저장
            dic[x] = i
        else:
            if dic[x] == -1:        # 이미 외톨이 알파벳이 되었다면, 넘어감
                continue
            elif i - dic[x] > 1:    # 이전 위치와 떨어져 있다면, 정답배열에 추가
                dic[x] = -1
                answer.append(x)
            else:                   # 하나의 덩어리로 뭉쳐져있다면, 인덱스 업데이트
                dic[x] = i
                
    if not answer:  # 배열이 비어있다면 "N"리턴
        return "N"
    else:           # 알파벳 정렬 후 str로 바꿔서 리턴
        answer.sort()       
        return "".join(answer)