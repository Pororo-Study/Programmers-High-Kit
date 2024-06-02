from collections import defaultdict

def solution(input_string):
    alpha = defaultdict(int)
    ans = set()
    answer = ''
    
    for i in range(len(input_string)):
        if alpha[input_string[i]]:
            if input_string[i] != input_string[i-1]:
                ans.add(input_string[i])
        alpha[input_string[i]] += 1
    
    ans = sorted(ans)
    answer = ''.join(ans)
    
    if answer == '':
        answer += "N"
         
    return answer