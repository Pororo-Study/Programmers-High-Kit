def solution(answers):
    answer = []
    score = [0, 0, 0]           # 점수
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 문제를 맞히면 점수에 1 더하기
    for i in range(len(answers)):
        if one[i % 5] == answers[i]:
            score[0] += 1
        if two[i % 8] == answers[i]:
            score[1] += 1
        if three[i % 10] == answers[i]:
            score[2] += 1
        
    # 최대 점수와 같으면 정답 배열에 추가
    max_score = max(score)
    for i in range(3):
        if score[i] == max_score:
            answer.append(i + 1)
    return answer