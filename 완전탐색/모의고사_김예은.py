def solution(answers):
    answer = []
    # 수포자들이 찍는 방식을 리스트로 생성
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    c1, c2, c3 = 0,0,0 # 수포자들이 몇개 맞았는지 저장
    
    for i in range(len(answers)):
        n1 = one[i%5] # 0(인덱스) % 5(원소개수) => 0번째 인덱스 확인 계속 순환됨.
        n2 = two[i%8]
        n3 = three[i%10]
        # 정답이 맞는지 체크하고 맞힌사람만 +1
        if n1 == answers[i]:
            c1 += 1
        if n2 == answers[i]:
            c2 += 1
        if n3 == answers[i]:
            c3 += 1

    k = max(c1, c2, c3) # 최대로 많이 맞힌 사람 구하고
    # 누가 맞힌지 출력(다중if문으로 같은 개수인 수포자 체크, 오름차순 해결)
    if k == c1:
        answer.append(1)
    if k == c2:
        answer.append(2)
    if k == c3:
        answer.append(3)
        
    return answer