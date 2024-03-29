import numpy as np
def solution(prices):

    n = len(prices)
    answer = [0] * n

    #stack에 주식 가격이 떨어지지 않은 기간 동안의 인덱스를 저장하자.
    stack = []

    for i in range(n):
        # 스택이 비어있지 않고, 현재 주식 가격이 이전 주식 가격보다 작을 때
        while stack and prices[i] < prices[stack[-1]]:
            # 이전 주식 가격이 떨어진 순간의 인덱스
            top = stack.pop()

            # 떨어진 기간 계산 및 저장
            answer[top] = i - top

            # 현재 인덱스 추가
        stack.append(i)

        # 주식 가격이 떨어지지 않은 기간 계산
    while stack:
        top = stack.pop()
        answer[top] = n - 1 - top

    return answer


"""
import numpy as np
def solution(prices):

    # 초 단위로 기록된 주식 가격이 담긴 배열 prices
    # 가격이 떨어지지 않은 기간은 몇 초인가?
    # np.where를 사용해보자
    answer = []
    for i, price in enumerate(prices):
        ind = np.where(np.array(prices) < price)
        flag = 0
        #len(ind[0]) == 0이라면 한 번도 떨어지지 않았다.
        #length - i - 1
        if len(ind[0]) == 0:
            sec = len(prices) - i - 1
            answer.append(sec)
        #len(ind[0]) != 0이라면 한 번이라도 떨어진 적이 있을 수 있다.
        #i보다 큰 인덱스 중에서 첫 번째를 기준으로 기간을 계산한다.
        else:
            for index in ind[0]:
                if index > i:
                    sec = index - i
                    answer.append(int(sec))
                    # 한 번이라도 떨어진 적이 있지만 과거 시점이었던 경우를 고려하는 flag
                    flag = 1
                    break

            if flag == 0:
                answer.append(len(prices) - i - 1)
    return answer
"""