from collections import defaultdict

def solution(clothes):
    # [의상의 이름, 의상의 종류]
    # 각 종류별 가진 의상을 저장 (종류:[이름, 이름, ...])
    closet = defaultdict(list) 
    for name, kind in clothes:
        closet[kind].append(name)
    
    # A의 종류가 N개, B의 종류가 M개 일 때 가능한 모든 경우의 수 (N+1)(M+1)
    answer = 1
    for _, value in closet.items():
        answer *= (len(value) + 1)
        
    return answer - 1