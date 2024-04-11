def solution(numbers):

    #numbers의 정수를 조합하여 만들 수 있는 가장 큰 수
    #큰 숫자가 먼저 와야한다.

    #조합은 시간 초과
    #numbers의 대소비교를 위해 str변환
    numbers = list(map(str, numbers))

    #큰 숫자가 먼저 오도록 numbers를 정렬한다
    #원소는 0이상 1000이하 이므로 x*4
    numbers.sort(key=lambda x: x*4, reverse=True)

    #0만 있는 경우 처리
    if numbers[0] == '0':
        answer = '0'
    else:
        #결과를 문자열로 바꿔서 return
        answer = ''.join(numbers)
    return answer