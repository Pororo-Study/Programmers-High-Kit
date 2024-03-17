def solution(arr):
    answer = [arr[0]]   # arr의 0번째 원소를 리스트에 넣어서 초기화
    
    for elem in arr:
        if elem != answer[-1]:  # arr의 원소가 answer의 마지막 원소와 다르면 추가
            answer.append(elem)
    
    return answer