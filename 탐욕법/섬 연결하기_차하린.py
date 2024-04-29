def solution(n, costs):
    # 0-1. 다리가 연결되는 두 섬의 번호
    # 2. 두 섬을 연결하는 다리를 건설할 때 드는 비용
    
    ans = 0
    # 비용 기준으로 오름차순 정렬
    costs.sort(key = lambda x:x[2])
    print(costs)
    link = set([costs[0][0]])
    
    while len(link) != n:
        for cost in costs:
            if cost[0] in link and cost[1] in link:
                continue
            if cost[0] in link or cost[1] in link:
                link.update([cost[0], cost[1]])
                ans += cost[2]
                break
    return ans