import numpy as np

def solution(scoville, K):
    # 스코빌 지수를 K이상으로 만들기 위한 Leo의 노력..
    # 새로운 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 스코빌 지수 * 2)
    # 모든 음식의 스코빌 지수가 k이상이 될 때까지 반복..대단하다
    # 섞어야 하는 최소 횟수

    answer = 0
    sorted_scoville = sorted(scoville)

    while len(sorted_scoville) != 1:
        ind = np.where(np.array(sorted_scoville) < K)
        if len(ind[0]) == 0:
            break
        else:
            new_scoville = sorted_scoville[0] + sorted_scoville[1] * 2
            sorted_scoville.pop(0)
            sorted_scoville.pop(0)
            sorted_scoville.append(new_scoville)
            sorted_scoville = sorted(sorted_scoville)
            answer += 1


    ind2 = np.where(np.array(sorted_scoville) >= K)
    if len(ind2[0]) == 0:
        answer = -1

    return answer