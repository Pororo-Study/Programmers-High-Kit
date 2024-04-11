def solution(array, commands):

    #array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때,
    #k번째에 있는 수를 구하려 한다.
    #commands = [i, j, k]로 이루어진 2차원 배열이다.

    answer = []
    for command in commands:
        #i, j번째 숫자와 k 할당
        i, j, k = command

        # j가 배열의 마지막 숫자를 가리키는 경우
        if j == len(array):
            cut_array = array[i-1:]
        else:
            cut_array = array[i-1:j]

        cut_array = sorted(cut_array)

        # k가 배열의 마지막 숫자를 가리키는 경우
        if k == len(cut_array):
            result = cut_array[-1]
        else:
            result = cut_array[k-1]

        answer.append(result)
    return answer