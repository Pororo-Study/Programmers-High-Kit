from itertools import permutations  # 순열
def solution(numbers):
    answer = 0
    for p_arr in permutations(numbers, len(numbers)):   # 순열 구하기
        temp_num = int(''.join([str(elem) for elem in p_arr]))  # 리스트의 모든 숫자들을 이어붙이기
        answer = max(answer, temp_num)  # 최댓값 구하기
    return str(answer)