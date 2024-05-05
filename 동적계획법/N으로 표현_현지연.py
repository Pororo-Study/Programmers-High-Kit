from collections import defaultdict

def solution(N, number):
    dic = defaultdict(set)  # key: 사용횟수, value: 만들 수 있는 숫자
    
    for i in range(1, 9):   # 1 ~ 8 반복
        dic[i].add(int(str(N) * i))     # 단순 초기화. 예) dic[3]에 NNN 넣기
        for x in dic[i]:
            if x == number:             # 원하는 숫자라면 return
                return i
            for j in range(1, 8 - i + 1):
                # 사칙연산 결과 넣어주기. 예) j가 3이라면 NNN과 사칙연산
                dic[i + j].add(x + int(str(N) * j))
                dic[i + j].add(x - int(str(N) * j))
                dic[i + j].add(x * int(str(N) * j))
                dic[i + j].add(x // int(str(N) * j))
                # 빼기와 나누기는 반대로 계산한 숫자도 넣어줌
                dic[i + j].add(int(str(N) * j) - x)
                if x != 0:
                    dic[i + j].add(int(str(N) * j) // x)
        
    return -1