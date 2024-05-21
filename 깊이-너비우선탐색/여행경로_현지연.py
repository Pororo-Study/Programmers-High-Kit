from collections import defaultdict

answer = [] # 정답 후보 배열

def dfs(tickets, departure, route): # (항공권 정보, 출발지, 경로)
    # 모든 항공권을 사용했다면, 경로를 정답 후보에 추가하기
    if len(tickets) == 0:
        answer.append(route)
        return
    # 항공권을 하나씩 확인하면서 출발지가 일치하다면 dfs 재귀적으로 호출
    for i in range(len(tickets)):
        if tickets[i][0] == departure:
            new_tickets = tickets[:i] + tickets[i+1:]   # 현재 항공권을 사용하고 나머지 항공권 배열
            dfs(new_tickets, tickets[i][1], route + [tickets[i][1]])

    
def solution(tickets):
    # 'ICN'에서 출발하는 항공권을 찾고 dfs 시작
    for i in range(len(tickets)):
        if tickets[i][0] == 'ICN':
            new_tickets = tickets[:i] + tickets[i+1:]   # 현재 항공권을 사용하고 나머지 항공권 배열
            dfs(new_tickets, tickets[i][1], ['ICN', tickets[i][1]])
    # 알파벳 순서대로 정렬 후, 첫번째 후보 리턴
    answer.sort()
    return answer[0]