def solution(brown, yellow):
    for h in range(3, brown):
        if (brown + yellow) % h == 0:       # brown + yellow의 약수 찾기 -> h
            w = (brown + yellow) // h       # 약수의 짝 구하기 -> w
            if 2 * w + 2 * h - 4 == brown:  # w와 h의 크기로 둘레 격자의 개수 구하기
                return [w, h]