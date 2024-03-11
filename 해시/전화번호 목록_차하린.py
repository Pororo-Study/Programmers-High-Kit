# 접두사
# 접사의 하나로 어떤 낱말 앞에 붙어서 의미를 첨가하여 한 다른 낱말을 이루는 말

# 풀이 1
# def solution(phone_book):
#     phone_book.sort()
#     for i in range(len(phone_book) - 1):
#         if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
#             return False
#     return True

# 풀이 2
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True

# startswith
# 현재 문자열이 사용자가 지정하는 특정 문자로 시작하는지 확인하는 함수