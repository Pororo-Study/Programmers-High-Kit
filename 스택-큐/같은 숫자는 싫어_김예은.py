
def solution(arr):
    answer = []
    answer.append(arr[0])
    top = 0
    for i in range(1, len(arr)):
        if arr[i] == answer[top]:
            continue
        else:
            answer.append(arr[i])
            top += 1
                        
    return answer