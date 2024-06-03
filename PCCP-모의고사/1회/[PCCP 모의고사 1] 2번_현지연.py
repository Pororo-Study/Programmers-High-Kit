from itertools import permutations  # 순열
def solution(ability):
    answer = 0
    for students in list(permutations(ability, len(ability[0]))):   # 종목 수 만큼 학생을 뽑고 나열
        sum_val = 0
        for i in range(len(ability[0])):                            # 0번째 학생은 0번 종목을 맡기
            sum_val += students[i][i]
        answer = max(answer, sum_val)                               # 최댓값 저장
    return answer