count = 0   # 방법의 수 count

def dfs(nums, tar, i, result):
    global count            # 전역변수
    if i == len(nums):
        if result == tar:
            count += 1
        return

    dfs(nums, tar, i + 1, result + nums[i]) # 숫자를 더하는 경우
    dfs(nums, tar, i + 1, result - nums[i]) # 숫자를 빼는 경우
        

def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return count