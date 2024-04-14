from itertools import permutations
ok = list()
def isPrime(n):
    # tuple 형태의 n을 list -> str -> int
    nums = list(n)
    string = ("").join(s for s in nums)
    num = int(string)
    # 소수 판별
    if num == 1 or num == 0: 
        return False
    for i in range(2, num):
        if num % i == 0: # 1과 자기자신으로 나누어지는 자연수는 소수 아님
            return False
    ok.append(num)
    cnt = ok.count(num) # 중복있는지 판별 numbers가 "011"인 경우 순열(11), (011)인 경우 모두 포함할 수 있음
    if cnt >= 2: # 중복된다면 False를 반환하여 answer값 증가하지 않도록 함 
        return False
    return True 

def solution(numbers):
    answer = 0
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i): # j는 tuple 형태
            result = isPrime(j) 
            if result == True: # 소수가 맞으면 answer 증가
                answer += 1
    return answer
