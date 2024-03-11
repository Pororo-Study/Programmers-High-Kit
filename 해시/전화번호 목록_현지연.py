def solution(phone_book):
    set_phone_book = set(phone_book)    # 집합으로 변환
    
    # 모든 전화번호를 각각 앞에서부터 슬라이싱 하면서 set_phone_book에 있는지 검사
    for elem in phone_book:                 # O(N)
        for i in range(len(elem)):
            if elem[:i] in set_phone_book:  # O(1)
                return False
    
    return True