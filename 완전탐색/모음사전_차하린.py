from itertools import product

def solution(word):
    idx = 0
    words = []
    alpha = ['A', 'E', 'I', 'O', 'U']
    
    for i in range(1, 6):
        for x in product(alpha, repeat = i):
            words.append(('').join((x)))
    words.sort()
    return words.index(word)+1
    