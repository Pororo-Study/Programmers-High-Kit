def solution(array, commands):
    answer = []                     # 정답 배열
    
    for i, j, k in commands:
        new_array = array[i - 1:j]      # 슬라이싱  # 최악의 경우 O(n)
        new_array.sort()                # 정렬      # O(nlogn)
        answer.append(new_array[k - 1]) # k번째에 있는 수 삽입
        
        # answer.append(sorted(array[i - 1:j])[k - 1])  # 한 줄 코드
        
    return answer

# array의 길이:n   commands의 길이:m
# O(2mnlogn + m) = O(mnlogn)