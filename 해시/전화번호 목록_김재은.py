import numpy as np
def solution(phone_book):


    phone_book = sorted(phone_book, key=len)
    result = True

    if len(phone_book[0]) == len(phone_book[-1]):
        return True
    else:
        #조회할 index 목록(0~20)
        list_index = np.zeros(21)
        for i in range(len(phone_book)):
            for j in range(1,21):
                if j == len(phone_book[i]):
                    list_index[j] = i
                    continue

        for number in phone_book:
            length = len(number)

            for k in range(int(list_index[length]), len(phone_book)):
                if phone_book[k][:length] == number:
                    result = False
                    break

        return result