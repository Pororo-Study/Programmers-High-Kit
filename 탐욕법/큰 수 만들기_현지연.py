def solution(number, k):
    stack = []  # 스택 사용
    
    for num in number:
        # 스택이 비어있지 않고, k가 0보다 크며, 스택의 마지막 원소가 현재 숫자보다 작은 경우
        while stack and k > 0 and stack[-1] < num:
            stack.pop()  # 스택의 마지막 원소 제거
            k -= 1  # 제거한 숫자 카운트
        stack.append(num)  # 현재 숫자를 스택에 추가
        
    if k != 0:  # 순회를 마친 후에도 k가 남은 경우, 스택의 끝에서부터 추가로 제거
        stack = stack[:-k]
        
    return ''.join(stack)  # 스택을 문자열로 변환하여 반환


# # 시간 초과 코드
# def solution(number, k):
#     answer = ''
#     number = list(number)
    
#     for _ in range(k):
#         # 앞에 숫자보다 뒤에 숫자가 클 경우, 앞에 숫자를 지움
#         check = False
#         for i in range(len(number) - 1):
#             if number[i] < number[i + 1]:
#                 del number[i]
#                 check = True
#                 break
#         # 마지막까지 지우지 못했을 경우, 마지막 숫자를 지움
#         if not check:
#             del number[i + 1]
            
#     return "".join(number)