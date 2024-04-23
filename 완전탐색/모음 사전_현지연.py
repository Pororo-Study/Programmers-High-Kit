from itertools import product   # 중복 허용 순열

def solution(word):
    arr = []                    # 사전 배열
    for i in range(1, 6):
        for per_word in list(product(['A', 'E', 'I', 'O', 'U'], repeat=i)):
            arr.append(''.join(per_word))
    arr.sort()
    return arr.index(word) + 1  # 배열에서 word의 인덱스 위치 찾기