def solution(answers):
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]

    scores = [0,0,0]

    for i, answer in enumerate(answers):
        if answer == student1[i % len(student1)]:
            scores[0] += 1
        if answer == student2[i % len(student2)]:
            scores[1] += 1
        if answer == student3[i % len(student3)]:
            scores[2] += 1

    top = max(scores)
    print(top)
    result = []
    for i in range(len(scores)):
        if scores[i] == top:
            result.append(i+1)

    return result