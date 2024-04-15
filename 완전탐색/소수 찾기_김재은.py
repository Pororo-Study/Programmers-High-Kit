from itertools import permutations

def solution(numbers):
    answer = []
    numbers = list(numbers)

    list_permutations = []
    for i in range(1, len(numbers) + 1):
        imsi = list(permutations(numbers, i))
        for permutation in imsi:
            list_permutations.append(int(('').join(permutation)))

    list_permutations = list(set(list_permutations))

    for number in list_permutations:
        if number < 2:
            continue

            # 소수 판별
        is_prime = True
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            answer.append(number)

    answer = len(set(answer))
    return answer