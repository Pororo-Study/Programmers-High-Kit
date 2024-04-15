def solution(brown, yellow):
    answer = []
    nums = []

    if yellow == 1: # yellow가 1개일때
        answer = [3,3] # 카펫의 가로 세로는 3,3
        return answer
    
    # 그 외
    # 갈색 격자의 수와 맞는 노란색 격자의 배치를 알기 위해 yellow의 약수를 구함(배치 = (가로*세로))
    for i in range(1, int(yellow**1/2)+1): # yellow의 약수를 구함
        if yellow % i == 0 :
            nums.append(i)
            
    nums.append(yellow)

    for i in nums: 
        j = yellow//i # i를 곱해서 yellow가 되는 수
        k = (i+j)*2+4 # (가로+세로)*2 + 4(모서리) -> 갈색 격자의 개수를 구함

        if k == brown: # 갈색 격자의 수와 맞는 노란색 격자 배치 형태를 구함
            if i>j: # 세로보다 더 긴 가로를 먼저 출력해야하므로 i, j 중 큰 것부터 가로, 세로 길이를 구하여 answer에 추가
                answer.append(i+2)
                answer.append(j+2)
            else:
                answer.append(j+2)
                answer.append(i+2)
            break
            
    return answer