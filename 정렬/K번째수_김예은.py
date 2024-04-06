def solution(array, commands):
    answer = []
    for com in commands: # commands는 [i,j,k]를 담은 2차원 배열
        # index 맞추기 위해 -1을 했다
        i = com[0]-1 
        j = com[1] # 슬라이싱 [i:j]는 i부터(포함) j까지(미포함)
        k = com[2]-1
        arr = sorted(array[i:j]) # 슬라이싱 후 정렬
        answer.append(arr[k]) 
    return answer