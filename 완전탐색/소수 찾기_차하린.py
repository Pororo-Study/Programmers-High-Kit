import math
from itertools import permutations

def primeNum(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    ans = 0
    numbers = [x for x in numbers]
    num = []
    for i in range(1, len(numbers)+1):
        num += list(permutations(numbers, i))
    
    nums = set()
    for n in num:
        nums.add(int(('').join(n)))
    
    for x in nums:
        if primeNum(x):
            ans += 1
    return ans