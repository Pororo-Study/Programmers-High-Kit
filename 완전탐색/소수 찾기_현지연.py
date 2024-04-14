from itertools import permutations
def solution(numbers):
    answer = []         # 소수 배열
    arr = set()         # 후보 숫자 집합
    
    # 완전 탐색으로 만들 수 있는 숫자를 집합에 넣음
    for i in range(1, len(numbers) + 1):
        p_list = list(permutations(numbers, i))
        for p in p_list:
            arr.add(int(''.join(p)))
    
    # 집합에 0 또는 1이 있을 경우 제거
    if 0 in arr:
        arr.remove(0)
    if 1 in arr:
        arr.remove(1)
        
    # 집합에 있는 숫자를 하나하나 소수인지 아닌지 확인
    for num in arr:
        check = True            # True: 소수, False: 합성수
        for i in range(2, num // 2 + 1):
            if num % i == 0:    # 합성수
                check = False
                break
        if check:
            answer.append(num)
        
    return len(answer)          # 소수의 개수 리턴