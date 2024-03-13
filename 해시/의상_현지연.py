# https://school.programmers.co.kr/learn/courses/30/lessons/42578
from collections import defaultdict

def solution(clothes):
    answer = 1              # 곱하기를 수행할 것이기 때문에 1로 초기화
    dic = defaultdict(int) 
    
    # key는 의상의 종류, value는 개수 딕셔너리에 저장
    for _, cloth_type in clothes:
        dic[cloth_type] += 1
        
    # 각 의상 종류의 개수에 1을 더해서 모두 곱해줌
    # 마지막에 1을 뺌(모두 선택되지 않은 경우) 
    for v in dic.values():
        answer *= (v + 1)
    return answer - 1