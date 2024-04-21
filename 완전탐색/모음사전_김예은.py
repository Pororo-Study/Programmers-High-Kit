from itertools import product

def solution(word):
    answer = 0

    # 만들 수 있는 단어 중복 순열로 생성
    lis = list()
    words = ['A','E','I','O','U']
    
    for j in range(1,6):
        for i in product(words,repeat=j):
            lis.append(list(i))

    lis.sort() # 사전순으로 만듦
    # print(lis)
    
    # word와 단어 비교
    for i in lis :
        answer += 1
        st = ''.join(s for s in i) # lis의 모든 단어들 리스트 -> 문자열로 만듦
        if (st == word):
            break
    return answer