def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers)) # 문자열 배열로 바꿔줌
    numbers.sort(key=lambda x:x*3, reverse=True) # 자리수(1000이하) 맞추기 위해 3번 반복, 내림차순 정렬
    
    # answer에 추가
    for i in numbers:
        answer += i
        
    # "00"인 경우 0으로 만들고 "0"으로 출력
    return str(int(answer))