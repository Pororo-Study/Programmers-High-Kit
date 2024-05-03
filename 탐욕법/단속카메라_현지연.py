def solution(routes):
    routes.sort(key=lambda x:x[1])  # 진출지점이 작은순으로 정렬
    stack = [routes[0]]             # 스택
    
    for a, b in routes[1:]:
        # 스택의 마지막 원소와 겹친다면 겹치는 부분으로 수정하기
        if a <= stack[-1][1]:
            stack[-1][0] = a
        # 겹치지 않는다면 스택에 추가하기
        else:
            stack.append([a, b])

    return len(stack)