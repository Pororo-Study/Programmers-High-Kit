def solution(arr):

    answer = []

    answer.append(arr[0])
    for number in arr:
        if number != answer[-1]:
            answer.append(number)

    return answer