def solution(nums):

    set_nums = set(nums)
    len_set_nums = len(set_nums)
    len_nums = len(nums)

    #len_nums는 항상 짝수입니다.
    if len_set_nums >= len_nums / 2:
        answer = len_nums / 2
    else:
        answer = len_set_nums

    return answer