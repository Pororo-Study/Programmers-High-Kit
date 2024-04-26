# def solution(number, k):
#     answer = ""
#     index = -1 # start(largest number's index)
#     for j in range(len(number) - k): # each position
#         max_char = '0'
#         c = k+j # end 2+0 2+1 / 3+0 3+1 3+2 3+3
#         for i in range(index + 1, c+ 1): # 큰 수 다음부터, c까지 최대값 검사
#             if max_char < number[i]:
#                 index = i
#                 max_char = number[i]
#         answer += max_char
#     return answer

# test case 10 시간초과

def solution(number, k):
    stack = []
    
    # 모든 원소를 stack에 넣어가면서
    # 현재 넣는 원소보다 stack의 맨 위 원소가 작을 경우
    # stack의 맨 위 원소 제거
    for num in number:
        while stack and stack[-1] < num and k>0:
            # stack 비어있지 않고 맨 앞 원소가 num보다 작고 아직 제거해야한다면 
            stack.pop() # 제거하고
            k -= 1 # 자리수 줄이기
            
        stack.append(num) # 일단 넣어
    # k가 남을 수도 있음
    # 뒷 원소 k만큼 자르기
    stack = stack[:len(number)-k]
        
    return ''.join(stack)
