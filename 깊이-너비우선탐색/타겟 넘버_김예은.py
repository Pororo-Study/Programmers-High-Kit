def solution(numbers, target):
    global answer
    answer = 0
    
    def dfs(n, total):
        global answer # 전역으로 선언하지않으면 if절에서 사용하는 answer를 로컬변수라고 생각. 
        if n == len(numbers): # 모든 numbers의 원소 순회했다면 (index out of bound check)
            if total == target: # 그리고 합이 target이면 answer +1 하고 반환
                answer += 1
            return
        # 재귀
        dfs(n+1, total+numbers[n]) # 다음원소를 더해보기
        dfs(n+1, total-numbers[n]) # 다음원소를 빼보기
        return
    dfs(0,0) # 시작
    return answer