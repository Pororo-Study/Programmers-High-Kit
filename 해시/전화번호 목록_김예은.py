from collections import defaultdict
def solution(phone_book):
    answer = True
        
    # 연속이어야함(한덩어리로, 작은 길이부터 확인)
    # 자리별 숫자 체크 
    check = defaultdict(list)
    num = ""
    
    for number in phone_book:
        for i in range(0, len(number)):
            if number[i] in check[i]:
                num += number[i]
                if num in phone_book:
                    return False
            else:
                check[i].append(number[i])
                
    return answer

print(solution(["123", "12","1234"]))