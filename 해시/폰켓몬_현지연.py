# 풀이 1
def solution(nums):
    answer = 0
    dic = dict()
    
    # dic에 폰켓몬의 종류 번호를 key로 저장
    for elem in nums:
        if elem not in dic:
            dic[elem] = 0
            
    # 폰켓몬의 종류 개수, N/2 값중 작은 값이 정답
    answer = min(len(dic.keys()), len(nums)//2)
    return answer

# # 풀이 2
# def solution(nums):
#     # 폰켓몬의 종류 개수, N/2 값중 작은 값이 정답
#     return min(len(set(nums)), len(nums)//2)