def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x : x[2]) # 비용을 기준으로 오름차순 정렬
    link = set([costs[0][0]]) # 시작
    print(costs)
    # kruskal 알고리즘
    while len(link) != n: # 모든 섬을 다돌면 끝남
        for v in costs:
            if v[0] in link and v[1] in link: # 섬 두개 모두 방문했다면 
                continue
            if v[0] in link or v[1] in link: # 섬 한 곳만 방문했더라도
                link.update([v[0], v[1]]) # 섬 두개 모두 추가(set type : 중복삭제됨)
                answer += v[2] # 비용추가
                break
    return answer