# def solution(nums):
#     unique = len(set(nums))
#     tmp = len(nums)
#     if tmp//2 > unique:
#         return unique
#     else:
#         return tmp//2
    
def solution(nums):
    return min(len(set(nums)), len(nums) // 2)